import json
path = r'd:\DOMO\2404\response_248150074.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
filters = data.get('page', {}).get('filters', [])
print(json.dumps(filters, ensure_ascii=False, indent=2))
