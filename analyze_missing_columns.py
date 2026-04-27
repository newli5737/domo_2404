"""
Exact Missing Column Reproducibility Table
===========================================
For each missing column, determine precisely whether it can be recreated:

PHYSICAL column → ❌ CANNOT recreate (raw data only exists in source DS)
FORMULA column  → Check if ALL physical columns from source DS exist in target DS:
  - YES (100% overlap) → ✅ CAN recreate (all base inputs available)
  - NO  (partial)      → ⚠️ MAYBE (formula may or may not use the missing physical cols)

Output: CSV + Markdown with one row per missing column.
"""
import json
import os
import sys
import re
import csv

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DIRECTORY = r"d:\DOMO\2404"


def load_har(har_path):
    with open(har_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_endpoint(har, page_id, endpoint_pattern):
    for entry in har['log']['entries']:
        url = entry['request']['url']
        if endpoint_pattern in url:
            text = entry.get('response', {}).get('content', {}).get('text', '')
            if text:
                try:
                    return json.loads(text)
                except:
                    pass
    return None


def analyze_page(har_path, page_id):
    har = load_har(har_path)
    analyzer = extract_endpoint(har, page_id, f'/pages/{page_id}/analyzer')
    stacks = extract_endpoint(har, page_id, f'/stacks/{page_id}/cards')
    
    if not analyzer or not stacks:
        return None

    page_title = stacks.get('page', {}).get('title', stacks.get('title', f'Page {page_id}'))
    data_sources = analyzer.get('details', {}).get('dataSources', [])

    if len(data_sources) <= 1:
        return None

    # Build per-dataset column info
    ds_info = {}
    for ds in data_sources:
        ds_id = ds.get('id', '')
        ds_name = ds.get('name', '')
        
        physical_cols = set()
        formula_cols = set()
        
        for col in (ds.get('columns') or []):
            col_name = col.get('name', '')
            if not col_name or col_name.startswith('calculation_') or re.match(r'^[a-f0-9-]{36}$', col_name):
                continue
            if col.get('isCalculation') or col.get('classType') == 'FORMULA':
                formula_cols.add(col_name)
            else:
                physical_cols.add(col_name)
        
        for formula in (ds.get('formulas') or []):
            f_name = formula.get('name', '')
            if f_name and not f_name.startswith('calculation_'):
                formula_cols.add(f_name)
        
        ds_info[ds_id] = {
            'name': ds_name,
            'physical': physical_cols,
            'formula': formula_cols,
            'all': physical_cols | formula_cols,
        }

    # Card -> dataset mapping
    cards = stacks.get('cards', [])
    card_datasets = {}
    for card in cards:
        card_id = card.get('id', '')
        card_type = card.get('type', '')
        chart_type = card.get('metadata', {}).get('chartType', '')
        if card_type != 'kpi': continue
        if any(x in chart_type for x in ['selector', 'slicer']): continue
        
        card_ds_ids = set()
        card_ds_names = []
        for ds in card.get('datasources', []):
            did = ds.get('dataSourceId', '')
            if did:
                card_ds_ids.add(did)
                card_ds_names.append(ds.get('dataSourceName', did))
        
        card_datasets[card_id] = {
            'title': card.get('title', ''),
            'ds_ids': card_ds_ids,
            'ds_names': card_ds_names,
        }

    # Build results: one row per (card, missing_column)
    rows = []
    for card_id, card_info in card_datasets.items():
        target_ds_ids = card_info['ds_ids']
        
        # Columns available in target (card's datasets)
        target_all = set()
        target_physical = set()
        for ds_id in target_ds_ids:
            if ds_id in ds_info:
                target_all |= ds_info[ds_id]['all']
                target_physical |= ds_info[ds_id]['physical']
        
        # Check each OTHER dataset on the page
        for source_ds_id, source_info in ds_info.items():
            if source_ds_id in target_ds_ids:
                continue
            
            # Pre-compute: do ALL source physical cols exist in target?
            source_phys = source_info['physical']
            missing_phys_from_source = source_phys - target_physical
            full_phys_overlap = len(missing_phys_from_source) == 0
            
            # Check each source column that's missing from target
            for col_name in sorted(source_info['all'] - target_all):
                is_formula = col_name in source_info['formula']
                
                if not is_formula:
                    # Physical column → cannot recreate
                    status = "❌ CANNOT"
                    reason = "Physical column - raw data chỉ tồn tại trong source dataset"
                elif full_phys_overlap:
                    # Formula + all source physical cols exist in target
                    status = "✅ CAN"
                    reason = "Tất cả physical columns của source dataset đều có trong target → formula có thể tạo lại"
                else:
                    # Formula but some source physical cols missing from target
                    status = "⚠️ MAYBE"
                    reason = f"Source DS thiếu {len(missing_phys_from_source)} physical cols trong target → cần check manual"
                
                rows.append({
                    'page_id': page_id,
                    'page_title': page_title,
                    'card_id': card_id,
                    'card_title': card_info['title'],
                    'card_dataset': ', '.join(card_info['ds_names']),
                    'missing_column': col_name,
                    'column_type': 'FORMULA' if is_formula else 'PHYSICAL',
                    'source_dataset': source_info['name'],
                    'can_recreate': status,
                    'reason': reason,
                })

    return {
        'page_id': page_id,
        'page_title': page_title,
        'ds_info': ds_info,
        'rows': rows,
    }


def main():
    har_files = []
    for f in os.listdir(DIRECTORY):
        if f.endswith('.com') or f.endswith('.har'):
            match = re.search(r'page_(\d+)', f)
            if match:
                har_files.append((os.path.join(DIRECTORY, f), match.group(1)))
    har_files.sort(key=lambda x: int(x[1]))

    all_pages = []
    all_rows = []

    for har_path, page_id in har_files:
        try:
            pd = analyze_page(har_path, page_id)
            if pd:
                all_pages.append(pd)
                all_rows.extend(pd['rows'])
                print(f"Page {page_id}: {len(pd['rows'])} missing column entries")
        except Exception as e:
            print(f"ERROR page {page_id}: {e}")
            import traceback; traceback.print_exc()

    # ===== CSV =====
    csv_path = os.path.join(DIRECTORY, "missing_columns_exact.csv")
    csv_keys = ['page_id', 'page_title', 'card_id', 'card_title', 'card_dataset',
                'missing_column', 'column_type', 'source_dataset', 'can_recreate', 'reason']
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=csv_keys)
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)
    print(f"\nCSV: {csv_path} ({len(all_rows)} rows)")

    # ===== Summary stats =====
    can_count = sum(1 for r in all_rows if '✅' in r['can_recreate'])
    maybe_count = sum(1 for r in all_rows if '⚠️' in r['can_recreate'])
    cannot_count = sum(1 for r in all_rows if '❌' in r['can_recreate'])
    print(f"✅ CAN recreate: {can_count}")
    print(f"⚠️ MAYBE: {maybe_count}")
    print(f"❌ CANNOT: {cannot_count}")

    # ===== Markdown Report =====
    md_path = os.path.join(DIRECTORY, "missing_columns_report.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Missing Columns - Exact Reproducibility\n\n")
        f.write("Mỗi missing column được phân loại chính xác:\n\n")
        f.write("| Status | Ý nghĩa |\n")
        f.write("|:---|:---|\n")
        f.write("| ✅ CAN | Formula - tất cả physical cols của source DS đều có trong target → **có thể tạo lại** |\n")
        f.write("| ⚠️ MAYBE | Formula - source DS có physical cols mà target thiếu → **cần check manual** |\n")
        f.write("| ❌ CANNOT | Physical column - raw data chỉ tồn tại trong source DS → **không thể tạo** |\n\n")
        f.write(f"**Tổng: ✅ {can_count} CAN | ⚠️ {maybe_count} MAYBE | ❌ {cannot_count} CANNOT**\n\n")

        for pd in all_pages:
            pid = pd['page_id']
            ptitle = pd['page_title']
            ds_info = pd['ds_info']
            rows = pd['rows']
            if not rows: continue

            f.write(f"\n---\n## {ptitle} (Page {pid})\n\n")

            # Dataset overview
            f.write("### Datasets\n")
            f.write("| Dataset | Physical | Formula |\n")
            f.write("|:---|:---:|:---:|\n")
            for ds_id, info in ds_info.items():
                f.write(f"| {info['name']} | {len(info['physical'])} | {len(info['formula'])} |\n")
            f.write("\n")

            # Group by (card_dataset, source_dataset) for cleaner view
            groups = {}
            for r in rows:
                key = (r['card_dataset'], r['source_dataset'])
                groups.setdefault(key, []).append(r)

            for (card_ds, source_ds), group_rows in groups.items():
                # Count unique cards
                unique_cards = set()
                for r in group_rows:
                    unique_cards.add((r['card_id'], r['card_title']))
                
                can = [r for r in group_rows if '✅' in r['can_recreate']]
                maybe = [r for r in group_rows if '⚠️' in r['can_recreate']]
                cannot = [r for r in group_rows if '❌' in r['can_recreate']]
                
                # Deduplicate: show unique columns (same for all cards with same DS)
                seen_cols = set()
                unique_can = []
                unique_maybe = []
                unique_cannot = []
                for r in can:
                    if r['missing_column'] not in seen_cols:
                        seen_cols.add(r['missing_column'])
                        unique_can.append(r)
                for r in maybe:
                    if r['missing_column'] not in seen_cols:
                        seen_cols.add(r['missing_column'])
                        unique_maybe.append(r)
                for r in cannot:
                    if r['missing_column'] not in seen_cols:
                        seen_cols.add(r['missing_column'])
                        unique_cannot.append(r)

                f.write(f"### Card DS: **{card_ds}** ← missing từ **{source_ds}**\n\n")
                f.write(f"*{len(unique_cards)} cards bị ảnh hưởng*\n\n")
                
                total_unique = len(unique_can) + len(unique_maybe) + len(unique_cannot)
                f.write(f"| Status | Missing Column | Type |\n")
                f.write(f"|:---:|:---|:---|\n")
                for r in unique_can:
                    f.write(f"| ✅ CAN | `{r['missing_column']}` | FORMULA |\n")
                for r in unique_maybe:
                    f.write(f"| ⚠️ MAYBE | `{r['missing_column']}` | FORMULA |\n")
                for r in unique_cannot:
                    f.write(f"| ❌ CANNOT | `{r['missing_column']}` | PHYSICAL |\n")
                f.write("\n")

    print(f"Report: {md_path}")


if __name__ == '__main__':
    main()
