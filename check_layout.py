import json
path = r'd:\DOMO\2404\response_248150074.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Page Keys:", data.get('page', {}).keys())
print("Page Filters:", data.get('page', {}).get('filters', []))

# Check Slicers in Layouts
layouts = data.get('page', {}).get('layouts', [])
if layouts:
    print(f"Found {len(layouts)} layouts")
    for layout in layouts:
        print(f"Layout type: {layout.get('type')}")
        cards = layout.get('cards', [])
        print(f"Cards in layout: {len(cards)}")
        for c in cards:
            cid = c.get('cardId')
            # Find card metadata
            card_obj = next((x for x in data.get('cards', []) if x.get('id') == cid), None)
            if card_obj:
                title = card_obj.get('title')
                ctype = card_obj.get('metadata', {}).get('chartType')
                if 'selector' in str(ctype) or 'slicer' in str(ctype):
                    print(f"  - Visible Slicer: {title} (ID: {cid}, Type: {ctype})")

# Check for Filters at the root level if any
if 'filters' in data:
    print("Root Filters:", data.get('filters'))
