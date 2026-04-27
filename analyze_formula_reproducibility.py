"""
DOMO Filter Views - Beastmode Reproducibility Analysis
======================================================
For each page with multiple datasets, analyze whether missing Formula columns 
from dataset A can potentially be recreated in dataset B.

Since HAR files do NOT contain formula expressions (stored server-side), 
we use physical column overlap as a proxy:
- If datasets share many physical columns, formulas are likely reproducible
- We also classify formulas vs physical columns and show actionable summary

Output: per-page cross-dataset comparison with column overlap and feasibility.
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
    """Deep analysis: for each dataset pair, check column overlap and formula reproducibility."""
    har = load_har(har_path)
    analyzer = extract_analyzer_data(har, page_id)
    stacks = extract_stacks_data(har, page_id)
    
    if not analyzer or not stacks:
        return None

    page_title = stacks.get('page', {}).get('title', stacks.get('title', f'Page {page_id}'))
    cards = stacks.get('cards', [])
    details = analyzer.get('details', {})
    data_sources = details.get('dataSources', [])

    if len(data_sources) <= 1:
        return None  # Single dataset = no cross-dataset issue

    # Build per-dataset column info
    ds_info = {}
    for ds in data_sources:
        ds_id = ds.get('id', '')
        ds_name = ds.get('name', '')
        
        physical_cols = set()
        formula_cols = set()
        all_col_names = set()
        
        for col in (ds.get('columns') or []):
            col_name = col.get('name', '')
            if not col_name: continue
            # Skip formula IDs
            if col_name.startswith('calculation_') or re.match(r'^[a-f0-9-]{36}$', col_name):
                continue
            all_col_names.add(col_name)
            if col.get('isCalculation') or col.get('classType') == 'FORMULA':
                formula_cols.add(col_name)
            else:
                physical_cols.add(col_name)
        
        for formula in (ds.get('formulas') or []):
            f_name = formula.get('name', '')
            if f_name and not f_name.startswith('calculation_'):
                formula_cols.add(f_name)
                all_col_names.add(f_name)
        
        ds_info[ds_id] = {
            'name': ds_name,
            'physical': physical_cols,
            'formula': formula_cols,
            'all': all_col_names,
        }

    # Get card-to-dataset mapping
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
            ds_id_val = ds.get('dataSourceId', '')
            if ds_id_val:
                card_ds_ids.add(ds_id_val)
                card_ds_names.append(ds.get('dataSourceName', ds_id_val))
        
        card_datasets[card_id] = {
            'title': card.get('title', ''),
            'ds_ids': card_ds_ids,
            'ds_names': card_ds_names,
            'chart_type': chart_type,
        }

    # For each card's dataset, find missing columns from OTHER datasets
    # and classify whether the missing formula could be recreated
    results = []
    
    for card_id, card_info in card_datasets.items():
        card_ds_ids = card_info['ds_ids']
        
        # Get ALL columns available in card's datasets
        card_physical = set()
        card_formula = set()
        card_all = set()
        for ds_id in card_ds_ids:
            if ds_id in ds_info:
                card_physical |= ds_info[ds_id]['physical']
                card_formula |= ds_info[ds_id]['formula']
                card_all |= ds_info[ds_id]['all']
        
        # For each OTHER dataset, find missing columns
        missing_analysis = []
        for source_ds_id, source_info in ds_info.items():
            if source_ds_id in card_ds_ids:
                continue  # Skip card's own dataset
            
            # Missing formulas = formulas in source DS but not in card's DS
            missing_formulas = source_info['formula'] - card_all
            # Missing physicals = physical cols in source DS but not in card's DS
            missing_physicals = source_info['physical'] - card_all
            
            if not missing_formulas and not missing_physicals:
                continue
            
            # Physical column overlap between source DS and card's DS
            # This tells us: how many of source's physical columns does the card also have?
            source_physical = source_info['physical']
            overlap_phys = card_physical & source_physical
            overlap_pct = (len(overlap_phys) / len(source_physical) * 100) if source_physical else 0
            
            missing_analysis.append({
                'source_ds_id': source_ds_id,
                'source_ds_name': source_info['name'],
                'missing_formulas': sorted(missing_formulas),
                'missing_physicals': sorted(missing_physicals),
                'source_physical_count': len(source_physical),
                'overlap_physical_count': len(overlap_phys),
                'overlap_pct': overlap_pct,
                'overlapping_cols': sorted(overlap_phys),
                'non_overlapping_cols': sorted(source_physical - overlap_phys),
            })
        
        if missing_analysis:
            results.append({
                'card_id': card_id,
                'card_title': card_info['title'],
                'card_datasets': ', '.join(card_info['ds_names']),
                'card_physical_count': len(card_physical),
                'missing_analysis': missing_analysis,
            })

    return {
        'page_id': page_id,
        'page_title': page_title,
        'ds_info': ds_info,
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

    all_pages = []
    csv_rows = []

    for har_path, page_id in har_files:
        try:
            print(f"Processing page {page_id}...")
            page_data = analyze_page(har_path, page_id)
            if page_data:
                all_pages.append(page_data)
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback; traceback.print_exc()

    # ===== CSV: One row per (card, source_dataset) pair =====
    csv_path = os.path.join(DIRECTORY, "formula_reproducibility.csv")
    csv_keys = ['page_id', 'page_title', 'card_id', 'card_title', 'card_datasets',
                'source_dataset', 'physical_overlap_pct', 'source_physical_count',
                'overlap_physical_count', 'missing_formula_count', 'missing_physical_count',
                'feasibility', 'missing_formulas', 'missing_physicals',
                'non_overlapping_physical_cols']
    
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=csv_keys)
        writer.writeheader()
        for pd in all_pages:
            for r in pd['results']:
                for ma in r['missing_analysis']:
                    pct = ma['overlap_pct']
                    if pct >= 80:
                        feasibility = "HIGH - Many shared columns"
                    elif pct >= 50:
                        feasibility = "MEDIUM - Partial overlap"
                    elif pct >= 20:
                        feasibility = "LOW - Few shared columns"
                    else:
                        feasibility = "VERY LOW - Almost no overlap"
                    
                    writer.writerow({
                        'page_id': pd['page_id'],
                        'page_title': pd['page_title'],
                        'card_id': r['card_id'],
                        'card_title': r['card_title'],
                        'card_datasets': r['card_datasets'],
                        'source_dataset': ma['source_ds_name'],
                        'physical_overlap_pct': f"{pct:.1f}%",
                        'source_physical_count': ma['source_physical_count'],
                        'overlap_physical_count': ma['overlap_physical_count'],
                        'missing_formula_count': len(ma['missing_formulas']),
                        'missing_physical_count': len(ma['missing_physicals']),
                        'feasibility': feasibility,
                        'missing_formulas': ' | '.join(ma['missing_formulas']),
                        'missing_physicals': ' | '.join(ma['missing_physicals']),
                        'non_overlapping_physical_cols': ' | '.join(ma['non_overlapping_cols']),
                    })
    print(f"\nCSV: {csv_path}")

    # ===== Markdown Report =====
    md_path = os.path.join(DIRECTORY, "formula_reproducibility_report.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Beastmode Formula Reproducibility Analysis\n\n")
        f.write("Phân tích khả năng tạo lại các beastmode (formula) bị thiếu ở dataset đích.\n\n")
        f.write("> **Lưu ý:** HAR files KHÔNG chứa formula expressions (được lưu server-side bởi DOMO).\n")
        f.write("> Phân tích dựa trên **physical column overlap** giữa dataset nguồn và dataset đích.\n")
        f.write("> Overlap cao = khả năng formula dùng các column chung → có thể tạo lại.\n\n")
        f.write("> **Feasibility levels:**\n")
        f.write("> - 🟢 **HIGH** (≥80% overlap) — Hầu hết physical columns giống nhau → formula rất có thể tạo lại\n")
        f.write("> - 🟡 **MEDIUM** (50-80%) — Khá nhiều columns chung → có thể tạo lại một phần\n")
        f.write("> - 🟠 **LOW** (20-50%) — Ít columns chung → khó tạo lại\n")
        f.write("> - 🔴 **VERY LOW** (<20%) — Gần như không có column chung → không thể tạo lại\n\n")

        for pd in all_pages:
            pid = pd['page_id']
            ptitle = pd['page_title']
            ds_info = pd['ds_info']
            results = pd['results']

            f.write(f"\n---\n## {ptitle} (Page {pid})\n\n")

            # Dataset overview
            f.write("### Datasets\n\n")
            f.write("| Dataset | Physical | Formula | Total |\n")
            f.write("|:---|:---:|:---:|:---:|\n")
            for ds_id, info in ds_info.items():
                f.write(f"| {info['name']} | {len(info['physical'])} | {len(info['formula'])} | {len(info['all'])} |\n")
            f.write("\n")

            # Cross-dataset overlap matrix
            ds_ids = list(ds_info.keys())
            if len(ds_ids) >= 2:
                f.write("### Physical Column Overlap Matrix\n\n")
                f.write("| Target \\ Source |")
                for ds_id in ds_ids:
                    f.write(f" {ds_info[ds_id]['name'][:20]} |")
                f.write("\n|:---|")
                for _ in ds_ids:
                    f.write(":---:|")
                f.write("\n")
                for t_id in ds_ids:
                    t_info = ds_info[t_id]
                    f.write(f"| {t_info['name'][:20]} |")
                    for s_id in ds_ids:
                        if s_id == t_id:
                            f.write(" - |")
                        else:
                            s_info = ds_info[s_id]
                            overlap = t_info['physical'] & s_info['physical']
                            pct = (len(overlap) / len(s_info['physical']) * 100) if s_info['physical'] else 0
                            emoji = "🟢" if pct >= 80 else "🟡" if pct >= 50 else "🟠" if pct >= 20 else "🔴"
                            f.write(f" {emoji} {pct:.0f}% ({len(overlap)}/{len(s_info['physical'])}) |")
                    f.write("\n")
                f.write("\n")

            # Group results by card dataset
            ds_groups = {}
            for r in results:
                key = r['card_datasets']
                ds_groups.setdefault(key, []).append(r)
            
            for ds_name, cards_in_ds in ds_groups.items():
                f.write(f"### Cards dùng: **{ds_name}** ({len(cards_in_ds)} cards)\n\n")
                
                # All cards with same dataset will have similar missing analysis
                sample = cards_in_ds[0]
                
                # Show card list
                f.write("<details><summary>Danh sách cards</summary>\n\n")
                for c in cards_in_ds:
                    f.write(f"- {c['card_title']} (Card {c['card_id']})\n")
                f.write("\n</details>\n\n")
                
                for ma in sample['missing_analysis']:
                    pct = ma['overlap_pct']
                    emoji = "🟢" if pct >= 80 else "🟡" if pct >= 50 else "🟠" if pct >= 20 else "🔴"
                    label = "HIGH" if pct >= 80 else "MEDIUM" if pct >= 50 else "LOW" if pct >= 20 else "VERY LOW"
                    
                    f.write(f"#### {emoji} Từ **{ma['source_ds_name']}** — Feasibility: **{label}** ({pct:.0f}% overlap)\n\n")
                    f.write(f"- Physical column overlap: **{ma['overlap_physical_count']}/{ma['source_physical_count']}**\n")
                    f.write(f"- Missing formulas: **{len(ma['missing_formulas'])}**\n")
                    f.write(f"- Missing physical cols: **{len(ma['missing_physicals'])}**\n\n")
                    
                    if ma['missing_formulas']:
                        f.write(f"**Missing Formulas** ({len(ma['missing_formulas'])}):\n")
                        for col in ma['missing_formulas'][:30]:
                            f.write(f"- `{col}`\n")
                        if len(ma['missing_formulas']) > 30:
                            f.write(f"- ... và {len(ma['missing_formulas']) - 30} nữa\n")
                        f.write("\n")
                    
                    if ma['non_overlapping_cols']:
                        f.write(f"**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):\n")
                        for col in ma['non_overlapping_cols'][:20]:
                            f.write(f"- `{col}`\n")
                        if len(ma['non_overlapping_cols']) > 20:
                            f.write(f"- ... và {len(ma['non_overlapping_cols']) - 20} nữa\n")
                        f.write("\n")

    print(f"Report: {md_path}")
    print(f"\nDone! {len(all_pages)} pages analyzed.")


if __name__ == '__main__':
    main()
