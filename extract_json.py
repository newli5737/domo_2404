import json
import sys
import os

def extract_stacks_json(har_path, output_path, page_id):
    if not os.path.exists(har_path):
        print(f"File not found: {har_path}")
        return False
        
    with open(har_path, 'r', encoding='utf-8') as f:
        try:
            har_data = json.load(f)
        except Exception as e:
            print(f"Error loading HAR {har_path}: {e}")
            return False
        
    for entry in har_data['log']['entries']:
        url = entry['request']['url']
        # Try different possible API patterns
        if f"/api/content/v3/stacks/{page_id}/cards" in url or \
           f"/api/content/v4/stacks/pages/{page_id}/cards" in url or \
           f"/api/content/v3/stacks/pages/{page_id}/cards" in url:
            
            if 'response' in entry and 'content' in entry['response'] and 'text' in entry['response']['content']:
                text = entry['response']['content']['text']
                try:
                    data = json.loads(text)
                    with open(output_path, 'w', encoding='utf-8') as out:
                        json.dump(data, out, ensure_ascii=False, indent=2)
                    print(f"Successfully extracted JSON to {output_path}")
                    return True
                except Exception as e:
                    print(f"Error parsing JSON text from {har_path}: {e}")
    
    print(f"Could not find stacks response for page {page_id} in {har_path}")
    return False

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        extract_stacks_json(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python extract_json.py <har_path> <output_path> <page_id>")
