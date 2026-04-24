"""
DOMO Filter Views Audit - Enhanced with Formula vs Physical Column Classification
==================================================================================
Parses HAR files to find which cards are missing Filter Views columns,
AND classifies each missing column as:
  - FORMULA (beastmode) → can potentially be recreated in the target dataset
  - COLUMN (physical)   → inherent to dataset, cannot be added via formula

Data sources:
- /api/content/v3/pages/{page_id}/analyzer -> details.dataSources[].columns 
  Each column has classType='COLUMN' (physical) or classType='FORMULA' (beastmode)
- /api/content/v3/stacks/{page_id}/cards -> cards[].datasources[].dataSourceId
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


def extract_analyzer_data(har, page_id):
    for entry in har['log']['entries']:
        url = entry['request']['url']
        if f'/pages/{page_id}/analyzer' in url:
            text = entry.get('response', {}).get('content', {}).get('text', '')
            if text:
                try:
                    return json.loads(text)
                except:
                    pass
    return None


def extract_stacks_data(har, page_id):
    for entry in har['log']['entries']:
        url = entry['request']['url']
        if f'/stacks/{page_id}/cards' in url:
            text = entry.get('response', {}).get('content', {}).get('text', '')
            if text:
                try:
                    return json.loads(text)
                except:
                    pass
    return None


def analyze_page(har_path, page_id):
    print(f"\n{'='*80}")
    print(f"Processing page {page_id}...")

    har = load_har(har_path)
    analyzer = extract_analyzer_data(har, page_id)
    stacks = extract_stacks_data(har, page_id)
    
    if not analyzer or not stacks:
        print(f"  WARNING: Missing analyzer or stacks data for page {page_id}")
        return None

    page_title = stacks.get('page', {}).get('title', stacks.get('title', f'Page {page_id}'))
    cards = stacks.get('cards', [])
    details = analyzer.get('details', {})
    data_sources = details.get('dataSources', [])

    # Build per-dataset info: columns + their classification
    ds_info = {}  # ds_id -> { 'name': str, 'columns': { col_name: 'FORMULA'|'COLUMN' } }
    ds_names = {}

    for ds in data_sources:
        ds_id = ds.get('id', '')
        ds_name = ds.get('name', '')
        ds_names[ds_id] = ds_name
        
        col_map = {}  # col_name -> classType
        for col in (ds.get('columns') or []):
            col_name = col.get('name', '')
            class_type = col.get('classType', 'COLUMN')
            if col.get('isCalculation'):
                class_type = 'FORMULA'
            if col_name:
                col_map[col_name] = class_type
            col_id = col.get('id', '')
            if col_id and col_id != col_name:
                col_map[col_id] = class_type
        
        # Also check formulas array (separate from columns in some pages)
        for formula in (ds.get('formulas') or []):
            f_name = formula.get('name', '')
            if f_name:
                col_map[f_name] = 'FORMULA'
            f_id = formula.get('id', '')
            if f_id and f_id != f_name:
                col_map[f_id] = 'FORMULA'

        ds_info[ds_id] = {'name': ds_name, 'columns': col_map}

    # Filter Views = union of all columns across all datasets (skip formula IDs)
    all_columns = {}  # col_name -> { 'class': FORMULA/COLUMN, 'source_ds': [ds_ids] }
    for ds_id, info in ds_info.items():
        for col_name, class_type in info['columns'].items():
            if col_name.startswith('calculation_') or re.match(r'^[a-f0-9-]{36}$', col_name):
                continue
            if col_name not in all_columns:
                all_columns[col_name] = {'class': class_type, 'source_ds': []}
            all_columns[col_name]['source_ds'].append(ds_id)
            # If ANY source has it as FORMULA, mark as FORMULA
            if class_type == 'FORMULA':
                all_columns[col_name]['class'] = 'FORMULA'

    print(f"  Page: {page_title}")
    print(f"  Datasets: {len(data_sources)}")
    for ds_id in ds_info:
        info = ds_info[ds_id]
        formula_count = sum(1 for v in info['columns'].values() if v == 'FORMULA')
        col_count = sum(1 for v in info['columns'].values() if v == 'COLUMN')
        print(f"    - {info['name']}: {col_count} physical + {formula_count} formulas")
    print(f"  Total Filter Views columns: {len(all_columns)}")

    # Analyze each card
    results = []
    for card in cards:
        card_id = card.get('id', '')
        card_title = card.get('title', 'Untitled')
        card_type = card.get('type', '')
        chart_type = card.get('metadata', {}).get('chartType', '')
        
        if card_type != 'kpi':
            continue
        if any(x in chart_type for x in ['selector', 'slicer']):
            continue

        # Card's dataset(s)
        card_ds_ids = set()
        card_ds_names = []
        for ds in card.get('datasources', []):
            ds_id = ds.get('dataSourceId', '')
            if ds_id:
                card_ds_ids.add(ds_id)
                card_ds_names.append(ds.get('dataSourceName', ds_id))

        # Columns available in card's datasets
        card_available = set()
        for ds_id in card_ds_ids:
            if ds_id in ds_info:
                card_available.update(ds_info[ds_id]['columns'].keys())

        # Missing columns
        missing_formulas = []
        missing_physicals = []
        for col_name, col_info in sorted(all_columns.items()):
            if col_name not in card_available:
                source_ds_names = [ds_names.get(sid, sid) for sid in col_info['source_ds']]
                entry = {
                    'column': col_name,
                    'class_type': col_info['class'],
                    'source_datasets': source_ds_names,
                }
                if col_info['class'] == 'FORMULA':
                    missing_formulas.append(entry)
                else:
                    missing_physicals.append(entry)

        results.append({
            'page_id': page_id,
            'page_title': page_title,
            'card_id': card_id,
            'card_title': card_title,
            'chart_type': chart_type,
            'card_datasets': ', '.join(card_ds_names),
            'card_ds_ids': card_ds_ids,
            'missing_formulas': missing_formulas,
            'missing_physicals': missing_physicals,
            'total_missing': len(missing_formulas) + len(missing_physicals),
            'url': f"https://astecpaints-co-jp.domo.com/page/{page_id}/kpis/details/{card_id}",
        })

    return {
        'page_id': page_id,
        'page_title': page_title,
        'datasets': ds_info,
        'ds_names': ds_names,
        'all_columns': all_columns,
        'results': results,
    }


def main():
    har_files = []
    for f in os.listdir(DIRECTORY):
        if f.endswith('.com') or f.endswith('.har'):
            match = re.search(r'page_(\d+)', f)
            if match:
                page_id = match.group(1)
            elif '248150074' in f:
                page_id = '248150074'
            else:
                continue
            har_files.append((os.path.join(DIRECTORY, f), page_id))

    har_files.sort(key=lambda x: int(x[1]))
    print(f"Found {len(har_files)} HAR files.")

    all_pages = []
    all_results = []

    for har_path, page_id in har_files:
        try:
            page_data = analyze_page(har_path, page_id)
            if page_data:
                all_pages.append(page_data)
                all_results.extend(page_data['results'])
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()

    # ===== CSV Output =====
    csv_path = os.path.join(DIRECTORY, "filter_views_audit_v2.csv")
    keys = ['page_id', 'page_title', 'card_id', 'card_title', 'chart_type',
            'card_datasets', 'missing_formula_count', 'missing_physical_count',
            'total_missing', 'missing_formulas', 'missing_physicals', 'url']
    
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in all_results:
            writer.writerow({
                'page_id': row['page_id'],
                'page_title': row['page_title'],
                'card_id': row['card_id'],
                'card_title': row['card_title'],
                'chart_type': row['chart_type'],
                'card_datasets': row['card_datasets'],
                'missing_formula_count': len(row['missing_formulas']),
                'missing_physical_count': len(row['missing_physicals']),
                'total_missing': row['total_missing'],
                'missing_formulas': ' | '.join(m['column'] for m in row['missing_formulas']),
                'missing_physicals': ' | '.join(m['column'] for m in row['missing_physicals']),
                'url': row['url'],
            })
    print(f"\nCSV saved: {csv_path}")

    # ===== Markdown Report =====
    md_path = os.path.join(DIRECTORY, "filter_views_report_v2.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# DOMO Filter Views Audit Report v2\n\n")
        f.write("Phân tích Filter Views với phân loại **FORMULA** (beastmode, có thể tạo lại) vs **COLUMN** (physical, không thể thêm).\n\n")
        f.write("> **Ký hiệu:**\n")
        f.write("> - 🟡 **FORMULA (Beastmode)** — Column này là công thức tính toán. Có thể tạo formula tương tự trong dataset đích.\n")
        f.write("> - 🔵 **COLUMN (Physical)** — Column vật lý chỉ tồn tại trong dataset nguồn. Không thể thêm vào dataset khác.\n\n")

        # Summary table
        f.write("## Tổng quan\n\n")
        f.write("| Page | Page Title | Datasets | Cards | Thiếu Formula | Thiếu Physical |\n")
        f.write("|:---|:---|:---:|:---:|:---:|:---:|\n")
        for pd in all_pages:
            results = pd['results']
            has_missing = [r for r in results if r['total_missing'] > 0]
            total_mf = sum(len(r['missing_formulas']) for r in results)
            total_mp = sum(len(r['missing_physicals']) for r in results)
            f.write(f"| {pd['page_id']} | {pd['page_title']} | {len(pd['datasets'])} | {len(results)} | {total_mf} | {total_mp} |\n")
        f.write("\n")

        for page_data in all_pages:
            pid = page_data['page_id']
            ptitle = page_data['page_title']
            ds_info = page_data['datasets']
            results = page_data['results']

            f.write(f"\n---\n## {ptitle} (Page {pid})\n\n")

            # Dataset info
            f.write("### Datasets\n\n")
            f.write("| Dataset | Physical Cols | Beastmodes |\n")
            f.write("|:---|:---:|:---:|\n")
            for ds_id, info in ds_info.items():
                phys = sum(1 for v in info['columns'].values() if v == 'COLUMN')
                form = sum(1 for v in info['columns'].values() if v == 'FORMULA')
                f.write(f"| {info['name']} | {phys} | {form} |\n")
            f.write("\n")

            if len(ds_info) <= 1:
                f.write("> ✅ Chỉ 1 dataset. Không có vấn đề cross-dataset.\n\n")
                continue

            missing_cards = [r for r in results if r['total_missing'] > 0]
            if not missing_cards:
                f.write("> ✅ Tất cả cards đã có đầy đủ columns.\n\n")
                continue

            # Group by dataset for cleaner view
            ds_groups = {}
            for r in missing_cards:
                key = r['card_datasets']
                ds_groups.setdefault(key, []).append(r)

            for ds_name, cards_in_ds in ds_groups.items():
                f.write(f"### Cards dùng dataset: **{ds_name}**\n\n")
                
                # Since all cards in same dataset will have same missing columns,
                # show the shared missing list first, then list card names
                sample = cards_in_ds[0]
                mf = sample['missing_formulas']
                mp = sample['missing_physicals']

                f.write(f"**{len(cards_in_ds)} cards** bị ảnh hưởng:\n")
                for c in cards_in_ds:
                    f.write(f"- {c['card_title']} (Card {c['card_id']}) — [Link]({c['url']})\n")
                f.write("\n")

                if mf:
                    f.write(f"#### 🟡 Missing Formulas (Beastmodes) — {len(mf)} columns — *có thể tạo lại*\n\n")
                    # Group by source dataset
                    by_src = {}
                    for m in mf:
                        for src in m['source_datasets']:
                            by_src.setdefault(src, []).append(m['column'])
                    for src, cols in by_src.items():
                        cols_display = cols[:30]
                        f.write(f"Từ **{src}**:\n")
                        for col in cols_display:
                            f.write(f"- `{col}`\n")
                        if len(cols) > 30:
                            f.write(f"- ... và {len(cols) - 30} beastmodes khác\n")
                        f.write("\n")

                if mp:
                    f.write(f"#### 🔵 Missing Physical Columns — {len(mp)} columns — *không thể thêm*\n\n")
                    by_src = {}
                    for m in mp:
                        for src in m['source_datasets']:
                            by_src.setdefault(src, []).append(m['column'])
                    for src, cols in by_src.items():
                        cols_display = cols[:30]
                        f.write(f"Từ **{src}**:\n")
                        for col in cols_display:
                            f.write(f"- `{col}`\n")
                        if len(cols) > 30:
                            f.write(f"- ... và {len(cols) - 30} physical columns khác\n")
                        f.write("\n")

    print(f"Markdown report saved: {md_path}")
    print(f"\n{'='*80}")
    print(f"SUMMARY: {len(all_pages)} pages, {len(all_results)} KPI cards")
    total_mf = sum(len(r['missing_formulas']) for r in all_results)
    total_mp = sum(len(r['missing_physicals']) for r in all_results)
    print(f"Total missing formula refs: {total_mf}")
    print(f"Total missing physical refs: {total_mp}")


if __name__ == '__main__':
    main()
