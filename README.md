# DOMO Filter Views Audit - 2404

Phân tích Filter Views (page-level column filters) cho 14 trang Dashboard DOMO.

## Vấn đề
Trên các page DOMO, nhiều card sử dụng các dataset khác nhau. Khi user chọn Filter Views column X, chỉ cards có dataset chứa column X mới phản ứng. Cards dùng dataset không có column X sẽ **không thay đổi**.

## Scripts

| File | Mô tả |
|:---|:---|
| `scan_filter_views.py` | **Script chính** — Parse HAR files, phân tích Filter Views, phân loại missing columns thành FORMULA (beastmode) vs COLUMN (physical) |
| `analyze_filters.py` | Script phân tích slicer-based filters (cũ) |
| `extract_json.py` | Extract JSON response từ HAR file |
| `process_all.py` | Batch process tất cả pages |
| `build_mapping.py` | Build column mapping |

## Output

| File | Mô tả |
|:---|:---|
| `filter_views_audit_v2.csv` | CSV chi tiết — phân loại FORMULA vs PHYSICAL |
| `filter_views_report_v2.md` | Markdown report chi tiết v2 |
| `filter_views_audit.csv` | CSV v1 (chưa phân loại) |
| `filter_views_report.md` | Markdown report v1 |
| `full_audit_results.csv` | Kết quả audit slicer-based (cũ) |

## Cách chạy

```bash
python scan_filter_views.py
```

Cần đặt HAR files (`.com` / `.har`) trong cùng thư mục. HAR files không được commit lên git vì quá nặng (50-145MB mỗi file).
