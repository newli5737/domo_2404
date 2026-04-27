"""
Clean Actionable Beastmode Report - Only ✅ CAN recreate
========================================================
Boss-friendly format: grouped by page → target dataset → list of formulas to create.
Output: CSV + clean Markdown report.
"""
import json, os, sys, re, csv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DIRECTORY = r"d:\DOMO\2404"


def load_har(har_path):
    with open(har_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_endpoint(har, page_id, pattern):
    for entry in har['log']['entries']:
        if pattern in entry['request']['url']:
            text = entry.get('response', {}).get('content', {}).get('text', '')
            if text:
                try: return json.loads(text)
                except: pass
    return None


def analyze_page(har_path, page_id):
    har = load_har(har_path)
    analyzer = extract_endpoint(har, page_id, f'/pages/{page_id}/analyzer')
    stacks = extract_endpoint(har, page_id, f'/stacks/{page_id}/cards')
    if not analyzer or not stacks: return None

    page_title = stacks.get('page', {}).get('title', stacks.get('title', ''))
    data_sources = analyzer.get('details', {}).get('dataSources', [])
    if len(data_sources) <= 1: return None

    # Build dataset info
    ds_info = {}
    for ds in data_sources:
        ds_id = ds.get('id', '')
        physical, formula = set(), set()
        for col in (ds.get('columns') or []):
            name = col.get('name', '')
            if not name or name.startswith('calculation_') or re.match(r'^[a-f0-9-]{36}$', name):
                continue
            if col.get('isCalculation') or col.get('classType') == 'FORMULA':
                formula.add(name)
            else:
                physical.add(name)
        for fm in (ds.get('formulas') or []):
            n = fm.get('name', '')
            if n and not n.startswith('calculation_'): formula.add(n)
        ds_info[ds_id] = {'name': ds.get('name', ''), 'physical': physical, 'formula': formula, 'all': physical | formula}

    # Card -> dataset
    cards = stacks.get('cards', [])
    card_ds = {}
    for card in cards:
        if card.get('type') != 'kpi': continue
        ct = card.get('metadata', {}).get('chartType', '')
        if any(x in ct for x in ['selector', 'slicer']): continue
        ds_ids = set()
        ds_names = []
        for d in card.get('datasources', []):
            did = d.get('dataSourceId', '')
            if did:
                ds_ids.add(did)
                ds_names.append(d.get('dataSourceName', did))
        card_ds[card.get('id', '')] = {'title': card.get('title', ''), 'ds_ids': ds_ids, 'ds_names': ds_names}

    # Find CAN recreate: missing FORMULA + 100% source physical overlap with target
    results = []  # unique (target_ds, source_ds, formula_name) tuples
    seen = set()

    for card_id, ci in card_ds.items():
        target_physical = set()
        for did in ci['ds_ids']:
            if did in ds_info: target_physical |= ds_info[did]['physical']
        target_all = set()
        for did in ci['ds_ids']:
            if did in ds_info: target_all |= ds_info[did]['all']

        for src_id, src in ds_info.items():
            if src_id in ci['ds_ids']: continue
            if not (src['physical'] <= target_physical): continue  # Not 100% overlap

            for col in sorted(src['formula'] - target_all):
                key = (tuple(ci['ds_names']), src['name'], col)
                if key not in seen:
                    seen.add(key)
                    results.append({
                        'page_id': page_id,
                        'page_title': page_title,
                        'target_dataset': ', '.join(ci['ds_names']),
                        'source_dataset': src['name'],
                        'beastmode_name': col,
                    })

    return {'page_id': page_id, 'page_title': page_title, 'ds_info': ds_info, 'results': results}


def main():
    har_files = []
    for f in os.listdir(DIRECTORY):
        if f.endswith('.com') or f.endswith('.har'):
            m = re.search(r'page_(\d+)', f)
            if m: har_files.append((os.path.join(DIRECTORY, f), m.group(1)))
    har_files.sort(key=lambda x: int(x[1]))

    all_pages = []
    all_rows = []
    for hp, pid in har_files:
        try:
            pd = analyze_page(hp, pid)
            if pd and pd['results']:
                all_pages.append(pd)
                all_rows.extend(pd['results'])
        except Exception as e:
            print(f"ERROR {pid}: {e}")

    # CSV
    csv_path = os.path.join(DIRECTORY, "beastmode_action_plan.csv")
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['page_id', 'page_title', 'target_dataset', 'source_dataset', 'beastmode_name'])
        w.writeheader()
        for r in all_rows: w.writerow(r)
    print(f"CSV: {csv_path} ({len(all_rows)} rows)")

    # Markdown
    md_path = os.path.join(DIRECTORY, "beastmode_action_plan.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Beastmode Action Plan\n\n")
        f.write("Danh sách các beastmode (formula) **CÓ THỂ tạo lại** trong dataset đích.\n\n")
        f.write("> Điều kiện: Tất cả physical columns của source dataset đều có trong target dataset\n")
        f.write("> → Formula có thể tạo lại với cùng syntax.\n\n")
        f.write(f"**Tổng: {len(all_rows)} beastmode cần tạo**\n\n")

        # Summary
        f.write("## Tổng quan\n\n")
        f.write("| Page | Tên Page | Số beastmode cần tạo |\n")
        f.write("|:---|:---|:---:|\n")
        for pd in all_pages:
            f.write(f"| {pd['page_id']} | {pd['page_title']} | {len(pd['results'])} |\n")
        f.write("\n")

        for pd in all_pages:
            f.write(f"\n---\n## {pd['page_title']} (Page {pd['page_id']})\n\n")

            # Group by (target, source)
            groups = {}
            for r in pd['results']:
                key = (r['target_dataset'], r['source_dataset'])
                groups.setdefault(key, []).append(r)

            for (tgt, src), rows in groups.items():
                f.write(f"### Tạo trong **{tgt}** (copy từ **{src}**)\n\n")
                f.write(f"| # | Beastmode cần tạo |\n")
                f.write(f"|:---:|:---|\n")
                for i, r in enumerate(rows, 1):
                    f.write(f"| {i} | `{r['beastmode_name']}` |\n")
                f.write("\n")

    print(f"Report: {md_path}")
    print(f"\nDone! {len(all_pages)} pages, {len(all_rows)} actionable beastmodes.")


if __name__ == '__main__':
    main()
