import json
import os

import sys

# Ensure utf-8 output for Japanese characters
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def normalize_str(s):
    if not s: return ""
    # Map half-width + to full-width ＋ and remove spaces
    return str(s).replace('+', '＋').replace(' ', '').lower()

def analyze_dashboard(response_path, page_id=None):
    if not os.path.exists(response_path):
        # We might want to return empty list here for programmatic usage
        if __name__ != "__main__":
            return []
        print(f"File not found: {response_path}")
        return

    with open(response_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cards = data.get('cards', [])
    page_title = data.get('page', {}).get('title', 'Unknown Page')
    if page_title == 'Unknown Page':
        page_title = data.get('title', 'Unknown Page')
    
    if not page_id:
        page_id = data.get('id', 'UnknownID')

    is_markdown = "--md" in sys.argv
    
    if not is_markdown:
        print(f"Analyzing Dashboard: {page_title} ({page_id})")
        print(f"Total Cards: {len(cards)}")
        print("-" * 50)

    # Build ID-to-Name mapping from all possible sources
    id_to_name = {}
    
    # 1. From Slicers
    for card in cards:
        chart_type = card.get('metadata', {}).get('chartType', '')
        if 'selector' in chart_type or chart_type in ['badge_slicer', 'badge_dropdown_selector', 'badge_checkbox_selector']:
            subs = card.get('subscriptions', [])
            if not subs: continue
            inner_sub = subs[0].get('subscription', {})
            for col in inner_sub.get('columns', []):
                if col.get('mapping') == 'ITEM':
                    id = col.get('column') or col.get('formulaId')
                    name = col.get('alias') or card.get('title')
                    if id and name: id_to_name[id] = name
            
    # 2. From definition.json (if available)
    def_path = os.path.join(os.path.dirname(response_path), "definition.json")
    if os.path.exists(def_path):
        try:
            with open(def_path, 'r', encoding='utf-8') as f:
                def_data = json.load(f)
                formulas = []
                if isinstance(def_data, dict):
                    formulas = def_data.get('definition', {}).get('formulas', [])
                elif isinstance(def_data, list):
                    for doc in def_data:
                        if isinstance(doc, dict):
                            formulas.extend(doc.get('formulas', []))
                
                for formula in formulas:
                    if 'id' in formula and 'name' in formula:
                        id_to_name[formula['id']] = formula['name']
        except: pass

    # 2. Extract Slicers
    slicers = []
    
    # Get visible card IDs from layout (handle different layout versions)
    visible_card_ids = set()
    layout_v4 = data.get('pageLayoutV4', {})
    
    # Version 1 (Standard)
    for item in layout_v4.get('standard', {}).get('content', []):
        if item.get('contentKey'): visible_card_ids.add(int(item.get('contentKey')))
    
    # Version 2 (Detailed items) - pageLayoutV4.content can be a list or dict
    content = layout_v4.get('content', [])
    if isinstance(content, dict):
        for item in content.get('items', []):
            if item.get('contentKey'): visible_card_ids.add(int(item.get('contentKey')))
    elif isinstance(content, list):
        for sub_layout in content:
            for item in sub_layout.get('items', []):
                if item.get('contentKey'): visible_card_ids.add(int(item.get('contentKey')))

    for card in cards:
        card_id = card.get('id')
        chart_type = card.get('metadata', {}).get('chartType', '')
        # ONLY include if it's a selector/slicer AND it's visible on the layout
        if 'selector' in chart_type or chart_type in ['badge_slicer', 'badge_dropdown_selector', 'badge_checkbox_selector']:
            # If dashboard has a layout, card MUST be in it to be considered a filter
            if layout_v4 and card_id not in visible_card_ids:
                continue
                
            internal_name = None
            for sub_item in card.get('subscriptions', []):
                inner_sub = sub_item.get('subscription', {})
                for col in inner_sub.get('columns', []):
                    if col.get('mapping') == 'ITEM':
                        internal_name = col.get('column') or col.get('formulaId')
                        break
                if internal_name: break
            
            if not internal_name and chart_type in ['badge_date_selector', 'badge_range_selector']:
                inner_sub = card.get('subscriptions', [{}])[0].get('subscription', {})
                internal_name = inner_sub.get('dateGrain', {}).get('column')

            if not internal_name: continue
            
            display_name = id_to_name.get(internal_name, card.get('title'))
            dataset_ids = set()
            dataset_names = set()
            for ds in card.get('datasources', []):
                if ds.get('dataSourceId'): dataset_ids.add(ds.get('dataSourceId'))
                if ds.get('dataSourceName'): dataset_names.add(normalize_str(ds.get('dataSourceName')))
            
            slicers.append({
                'display_name': display_name,
                'internal_name': internal_name,
                'dataset_ids': dataset_ids,
                'dataset_names': dataset_names
            })

    # 2.5 Add Page Level Filters from page.filters
    page_filters = data.get('page', {}).get('filters', [])
    for pf in page_filters:
        col_id = pf.get('column')
        if not col_id: continue
        display_name = id_to_name.get(col_id, col_id)
        # We don't have dataset info for page filters easily, but we know they exist.
        slicers.append({
            'display_name': display_name,
            'internal_name': col_id,
            'dataset_ids': set(), # Global page filter
            'dataset_names': set()
        })
    
    # Perform Audit
    results = []
    for card in cards:
        # Skip non-KPI cards (like Text cards/Memos)
        if card.get('type') != 'kpi':
            continue
            
        card_id = card.get('id')
        title = card.get('title')
        chart_type = card.get('metadata', {}).get('chartType', '')
        
        # KPI dataset IDs
        kpi_dataset_ids = set()
        for ds in card.get('datasources', []):
            if ds.get('dataSourceId'): kpi_dataset_ids.add(ds.get('dataSourceId'))
            
        # Used columns from subscriptions
        used_cols = set()
        subs = card.get('subscriptions', [])
        for sub_item in subs:
            subscription = sub_item.get('subscription', {})
            for c in subscription.get('columns', []):
                col_id = c.get('column') or c.get('formulaId')
                if col_id: 
                    used_cols.add(col_id)
                    if col_id in id_to_name: used_cols.add(id_to_name[col_id])
            for f in subscription.get('filters', []):
                f_id = f.get('column')
                if f_id: 
                    used_cols.add(f_id)
                    if f_id in id_to_name: used_cols.add(id_to_name[f_id])
        
        # Check date range
        date_info = card.get('dateInfo', {})
        if date_info:
            date_col = date_info.get('dateRange', {}).get('columnName')
            if date_col: 
                used_cols.add(date_col)
                if date_col in id_to_name: used_cols.add(id_to_name[date_col])

        # Collect dataset names for fuzzy matching
        kpi_dataset_names = set()
        for ds in card.get('datasources', []):
            if ds.get('dataSourceName'): kpi_dataset_names.add(normalize_str(ds.get('dataSourceName')))

        # Check each slicer against this card
        missing_splicer_names = []
        card_json_str = json.dumps(card, ensure_ascii=False)
        for slicer in slicers:
            # 1. shared dataset ID?
            if kpi_dataset_ids.intersection(slicer['dataset_ids']):
                continue 
            
            # 2. fuzzy dataset name match? (Clones or closely related datasets)
            found_fuzzy = False
            for kpi_ds_name in kpi_dataset_names:
                for slicer_ds_name in slicer.get('dataset_names', []):
                    # Check if one is a version/subset of the other
                    if slicer_ds_name in kpi_ds_name or kpi_ds_name in slicer_ds_name:
                        found_fuzzy = True; break
                    # OR check common prefix of 4+ characters
                    if len(slicer_ds_name) > 3 and len(kpi_ds_name) > 3:
                        if slicer_ds_name[:4] == kpi_ds_name[:4]:
                            found_fuzzy = True; break
                if found_fuzzy: break
            if found_fuzzy: continue

            # 3. explicit match (ID or Name)?
            if slicer['internal_name'] in used_cols or slicer['display_name'] in used_cols:
                continue

            # 4. Fallback: Substring match in JSON
            if slicer['display_name'] in card_json_str:
                continue
            
            missing_splicer_names.append(slicer['display_name'])

        results.append({
            'page_id': page_id,
            'page_title': page_title,
            'card_id': card_id,
            'title': title,
            'chart_type': chart_type,
            'url': f"https://astecpaints-co-jp.domo.com/page/{page_id}/kpis/details/{card_id}",
            'missing_fields': missing_splicer_names,
            'status': "🔴 Thiếu" if missing_splicer_names else "🟢 Đủ"
        })

    # Output report
    if is_markdown:
        print(f"\n### Dashboard: {page_title} ({page_id})")
        all_slicer_names = [s['display_name'] for s in slicers]
        print("\n**Bộ lọc trang (Slicers):** " + (", ".join(f"`{c}`" for c in all_slicer_names) if all_slicer_names else "Không có"))
        print("\n| Card ID | Tiêu đề Card | Trạng thái | Field còn thiếu | URL |")
        print("|:---|:---|:---|:---|:---|")
    else:
        print(f"\nAnalyzing Dashboard: {page_title} ({page_id})")
        print(f"Total Cards: {len(cards)}")
        print("-" * 50)
        print(f"{'Card ID':<12} | {'Card Title':<40} | {'Status':<10} | {'Missing Fields'}")
        print("-" * 120)
    
    for res in results:
        # Format missing fields as a clean string for CSV/Markdown
        missing_str = ", ".join(res['missing_fields']) if res['missing_fields'] else "-"
        res['missing_fields_str'] = missing_str
        
        if is_markdown:
            print(f"| {res['card_id']} | {res['title']} | {res['status']} | {missing_str} | [Link]({res['url']}) |")
        else:
            display_title = (res['title'][:37] + '...') if len(res['title']) > 40 else res['title']
            print(f"{res['card_id']:<12} | {display_title:<40} | {res['status']:<10} | {missing_str}")

    # For programmatic return, ensure missing_fields is a string for the CSV writer
    for res in results:
        res['missing_fields'] = res['missing_fields_str']
        del res['missing_fields_str']

    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_dashboard(sys.argv[1])
    else:
        # Default for first page
        analyze_dashboard(r'd:\DOMO\2404\response.json')

