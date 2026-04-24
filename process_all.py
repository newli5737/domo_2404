import os
import subprocess
import re
import csv
import sys

# Import the analysis function directly for better control
from analyze_filters import analyze_dashboard

def process_all():
    directory = r"d:\DOMO\2404"
    files = [f for f in os.listdir(directory) if f.endswith(".com") or f.endswith(".har")]
    
    # Target 14 pages
    target_pattern = r"page_(\d+)"
    
    all_cards_data = []
    final_report_content = "# Báo cáo Chi tiết Kiểm tra Bộ lọc 14 Dashboard DOMO\n\n"
    final_report_content += "Dưới đây là bảng phân tích chi tiết cho từng Card trong 14 trang Dashboard.\n\n"
    final_report_content += "> [!NOTE]\n"
    final_report_content += "> - **🟢 Đủ**: Card có đầy đủ các field cần thiết.\n"
    final_report_content += "> - **🔴 Thiếu**: Card thiếu field Subscription, không cập nhật khi lọc Dashboard.\n\n---\n"
    
    for filename in sorted(files):
        match = re.search(target_pattern, filename)
        if not match:
            if "248150074" in filename:
                page_id = "248150074"
            else:
                continue
        else:
            page_id = match.group(1)
            
        print(f"Processing Page {page_id} from {filename}...")
        
        har_path = os.path.join(directory, filename)
        json_path = os.path.join(directory, f"response_{page_id}.json")
        
        # 1. Extract JSON
        subprocess.run(["python", "d:/DOMO/2404/extract_json.py", har_path, json_path, page_id])
        
        if os.path.exists(json_path):
            # 2. Analyze Filter - Capturing Markdown for the report
            # We use a trick: capture stdout but also call programmatically to get data
            
            # Temporarily set sys.argv for the subprocess-like behavior in the same process
            original_argv = sys.argv
            sys.argv = [sys.argv[0], json_path, "--md"]
            
            # Use a context manager to capture stdout for the markdown report
            import io
            from contextlib import redirect_stdout
            
            f = io.StringIO()
            with redirect_stdout(f):
                page_data = analyze_dashboard(json_path, page_id)
            
            sys.argv = original_argv
            
            final_report_content += f.getvalue() + "\n---\n"
            all_cards_data.extend(page_data)
        else:
            print(f"Failed to extract JSON for {page_id}")

    # Output Markdown report
    report_path = os.path.join(directory, "final_report_full.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(final_report_content)
    
    # Output CSV report
    csv_path = os.path.join(directory, "full_audit_results.csv")
    if all_cards_data:
        keys = ['page_id', 'page_title', 'card_id', 'title', 'chart_type', 'status', 'missing_fields', 'url']
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            # Clean data for CSV
            for row in all_cards_data:
                clean_row = {k: row[k] for k in keys}
                dict_writer.writerow(clean_row)
    
    print(f"\nDone!")
    print(f"- Full Markdown report: {report_path}")
    print(f"- Full CSV report: {csv_path}")

if __name__ == "__main__":
    process_all()
