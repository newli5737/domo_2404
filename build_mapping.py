import json
import os
import glob
import re

def build_global_map(directory):
    id_to_name = {}
    
    # Scan all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, "response*.json"))
    json_files.append(os.path.join(directory, "response.json"))
    json_files.append(os.path.join(directory, "definition.json"))
    
    for file_path in json_files:
        if not os.path.exists(file_path): continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Search for IDs and Names
                # Pattern 1: Slicer structure
                cards = []
                if isinstance(data, dict):
                    cards = data.get('cards', [])
                elif isinstance(data, list):
                    cards = [c for doc in data if isinstance(doc, dict) for c in doc.get('cards', [])]
                
                for card in cards:
                    # From slicer columns
                    subs = card.get('subscriptions', [])
                    for sub_item in subs:
                        inner_sub = sub_item.get('subscription', {})
                        for col in inner_sub.get('columns', []):
                            id = col.get('column') or col.get('formulaId')
                            name = col.get('alias')
                            if id and name: id_to_name[id] = name
                    
                    # From card title (if it is a slicer)
                    chart_type = card.get('metadata', {}).get('chartType', '')
                    if 'selector' in chart_type or 'badge_slicer' in chart_type:
                        for sub_item in card.get('subscriptions', []):
                            inner_sub = sub_item.get('subscription', {})
                            for col in inner_sub.get('columns', []):
                                if col.get('mapping') == 'ITEM':
                                    id = col.get('column') or col.get('formulaId')
                                    if id: id_to_name[id] = card.get('title')
                                    
                # Pattern 2: formulas block (definition.json)
                formulas = []
                if isinstance(data, dict):
                    formulas = data.get('definition', {}).get('formulas', [])
                elif isinstance(data, list):
                    for doc in data:
                        if isinstance(doc, dict):
                            formulas.extend(doc.get('formulas', []))
                
                for formula in formulas:
                    if 'id' in formula and 'name' in formula:
                        id_to_name[formula['id']] = formula['name']
                        
        except: continue
        
    return id_to_name

if __name__ == "__main__":
    dir_path = r'd:\DOMO\2404'
    mapping = build_global_map(dir_path)
    with open(os.path.join(dir_path, 'global_mapping.json'), 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print("Mapping built successfully in global_mapping.json")
