# DOMO Filter Views Audit Report

Phân tích Filter Views (page-level column filters) cho các trang Dashboard DOMO.

> **Cách DOMO Filter Views hoạt động:**
> - Filter Views hiển thị TẤT CẢ columns từ TẤT CẢ datasets trên page.
> - Khi user chọn filter column X, chỉ cards có dataset chứa column X mới bị filter.
> - Cards dùng dataset KHÔNG có column X sẽ **KHÔNG phản ứng** với filter.

## Tổng quan

| Page | Page Title | Datasets | Cards | Cards có missing |
|:---|:---|:---:|:---:|:---:|
| 193413623 | 工場アパマンチームのキーエンス指標 | 1 | 6 | 0 |
| 213860614 | 施工店分析 | 3 | 25 | 25 |
| 248150074 | 工場売上分析 | 3 | 14 | 14 |
| 836254252 | 物件種別修正用 | 4 | 3 | 3 |
| 929628649 | 完工予測 | 3 | 16 | 16 |
| 1134665337 | プロテック案件実績 | 4 | 20 | 20 |
| 1206453601 | アパマン売上分析 | 2 | 13 | 13 |
| 1281028522 | 商談未確定・郵送件数検索 | 2 | 18 | 18 |
| 1377736771 | 商談・現調案件検索 | 1 | 20 | 0 |
| 1428843185 | コラボス集計 | 3 | 36 | 36 |
| 1774230854 | プロテックチームのキーエンス指標 | 1 | 6 | 0 |
| 1827358914 | 全体管理 | 4 | 47 | 47 |
| 1959758463 | 週間MTG用コラボス分析 | 2 | 16 | 16 |
| 2006619322 | 法人営業部用_売上集計(出荷日基準) | 4 | 4 | 4 |


---
## 工場アパマンチームのキーエンス指標 (Page 193413623)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| Zoho統合データ | `01b6c4e7-181...` | 287 |

> ✅ Tất cả cards dùng cùng dataset. Không có vấn đề Filter Views cross-dataset.


---
## 施工店分析 (Page 213860614)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| コラボス_契約率移動平均用 | `97b86f0a-3e0...` | 21 |
| コラボス＋リペイント | `d767503e-113...` | 380 |
| コラボス＋リペイント（昨対集計用） | `6c6260a1-763...` | 11 |

**Tổng card KPI:** 25 | **Sẽ KHÔNG phản ứng với một số filter:** 25 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 数値進捗（施工店）3ヶ月集計 (Card 206632515)
- **Dataset:** コラボス＋リペイント（昨対集計用）
- **Columns có:** 11 | **Thiếu:** 255 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/206632515)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `元請会社（DCMまとめ）`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `担当センター`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`, `都道府県`
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 224 columns khác

#### 🔴 数値進捗（施工店） (Card 118066549)
- **Dataset:** コラボス＋リペイント（昨対集計用）
- **Columns có:** 11 | **Thiếu:** 255 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/118066549)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `元請会社（DCMまとめ）`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `担当センター`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`, `都道府県`
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 224 columns khác

#### 🔴 契約率（12ヶ月移動平均） (Card 532453145)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 247 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/532453145)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `カテゴリ`, `カテゴリ表示順`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 契約率（3ヶ月移動平均） (Card 1866181173)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 247 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1866181173)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `カテゴリ`, `カテゴリ表示順`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 未完工一覧 (Card 633141134)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/633141134)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 契約一覧(見積結果日基準) (Card 1931412914)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1931412914)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 平均単価(施工店請負金額) (Card 1851405345)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1851405345)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 商談未確定率（見積提案日基準） (Card 1969287996)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1969287996)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 月別施工店ごと商談未確定件数(今期) (Card 138189276)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/138189276)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 見積数（見積提案日基準） (Card 53616018)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/53616018)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 契約数(結果確定日基準) (Card 710284790)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/710284790)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 案件一覧(施工店用_承り日基準) (Card 1465358268)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1465358268)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 完工一覧（工事完了予定日基準） (Card 2147160344)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/2147160344)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 案件数（承り日基準） (Card 395356149)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/395356149)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 平均日数（施工店別） (Card 595232334)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/595232334)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 郵送率（施工店でフィルター必須） (Card 831102014)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/831102014)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 郵送率（3ヶ月毎） (Card 1288974591)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1288974591)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 見積件数一覧(見積提案日基準) (Card 765442322)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/765442322)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 元請け別契約金額(結果確定日基準) (Card 1579225174)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1579225174)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 契約率(施工店分析） (Card 90992398)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/90992398)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 完工一覧 (Card 1123284518)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1123284518)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 月別施工店ごと郵送件数(今期) (Card 868287800)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/868287800)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 元請け別完工金額 (Card 1715340574)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1715340574)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 商談未確定率（3ヶ月毎） (Card 1137777881)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1137777881)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`

#### 🔴 契約率_グラフ（見積提案日基準） (Card 1010684648)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1010684648)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`


---
## 工場売上分析 (Page 248150074)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| ER_売上/受注_直近_PRD | `d7d0cd1d-121...` | 887 |
| ER_現場名入り売上実績 | `92c0b6fd-4c0...` | 317 |
| 【大型出荷有無用】ER_売上/受注_直近_PRD | `fa32aa9b-882...` | 25 |

**Tổng card KPI:** 14 | **Sẽ KHÔNG phản ứng với một số filter:** 14 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 月別_工場・倉庫・施設出荷社数 (Card 1017947390)
- **Dataset:** 【大型出荷有無用】ER_売上/受注_直近_PRD
- **Columns có:** 25 | **Thiếu:** 592 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1017947390)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `AP/PT種別区分`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)` ... và 522 columns khác
  - Từ **ER_現場名入り売上実績**: `AP/PT種別区分`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名(受注時)`, `AP営業所名(実績担当基準)`, `AP担当者ID`, `AP担当者ID(受注時)`, `AP担当者名(受注時)`, `CX出荷社数` ... và 259 columns khác

#### 🔴 出荷済社数_工場・施設 (Card 1734810736)
- **Dataset:** 【大型出荷有無用】ER_売上/受注_直近_PRD
- **Columns có:** 25 | **Thiếu:** 592 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1734810736)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `AP/PT種別区分`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)` ... và 522 columns khác
  - Từ **ER_現場名入り売上実績**: `AP/PT種別区分`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名(受注時)`, `AP営業所名(実績担当基準)`, `AP担当者ID`, `AP担当者ID(受注時)`, `AP担当者名(受注時)`, `CX出荷社数` ... và 259 columns khác

#### 🔴 工場案件一覧 (Card 1643529095)
- **Dataset:** ER_現場名入り売上実績
- **Columns có:** 317 | **Thiếu:** 319 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1643529095)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID` ... và 295 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `加盟店子ランク表示順`, `売上時期`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設出荷社数_年比較 (Card 228624032)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/228624032)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 商品別_工場・倉庫・施設出荷現場数 (Card 674045266)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/674045266)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設売上 (Card 1924842861)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1924842861)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 商品別_工場・倉庫・施設出荷社数 (Card 1341591185)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1341591185)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設出荷現場数 (Card 572002633)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/572002633)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設出荷_平均単価_年比較 (Card 571321567)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/571321567)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設売上_年比較 (Card 1712590684)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1712590684)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設出荷現場数_年比較 (Card 335358071)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/335358071)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 商品別_工場・倉庫・施設出荷_平均単価 (Card 988661802)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/988661802)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_工場・倉庫・施設出荷_平均単価 (Card 1491562448)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1491562448)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 材料別_工場・倉庫・施設売上 (Card 647931224)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 54 / 611
- **[Xem card](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/647931224)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_現場名入り売上実績**: `CX出荷社数`, `CX加盟店出荷社数`, `ER_現場名(制限あり).company_id`, `SC元請出荷社数`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `note`, `office_id` ... và 30 columns khác
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`


---
## 物件種別修正用 (Page 836254252)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| ER_売上/受注_直近_PRD | `d7d0cd1d-121...` | 887 |
| ER_現場名入り売上実績 | `92c0b6fd-4c0...` | 317 |
| Store Example Data | `1cd1946f-e23...` | 5 |
| コラボス＋リペイント | `d767503e-113...` | 380 |

**Tổng card KPI:** 3 | **Sẽ KHÔNG phản ứng với một số filter:** 3 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 物件種別修正用一覧_コラボス (Card 936888329)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 568 / 817
- **[Xem card](https://astecpaints-co-jp.domo.com/page/836254252/kpis/details/936888329)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_現場名入り売上実績**: `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID`, `AP担当者ID(受注時)`, `AP担当者名` ... và 230 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 ERAWAN_物件種別(すべて) (Card 916494563)
- **Dataset:** ER_現場名入り売上実績
- **Columns có:** 317 | **Thiếu:** 525 / 817
- **[Xem card](https://astecpaints-co-jp.domo.com/page/836254252/kpis/details/916494563)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID` ... và 295 columns khác
  - Từ **コラボス＋リペイント**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ROW_NUM_`, `calendar_date`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `その他の詳細`, `カテゴリ表示順`, `キャンペーン`, `コラボスデータ`, `コーナン_加盟金あり` ... và 187 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 物件種別修正用一覧_ERAWAN (Card 1675340749)
- **Dataset:** ER_現場名入り売上実績
- **Columns có:** 317 | **Thiếu:** 525 / 817
- **[Xem card](https://astecpaints-co-jp.domo.com/page/836254252/kpis/details/1675340749)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID` ... và 295 columns khác
  - Từ **コラボス＋リペイント**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ROW_NUM_`, `calendar_date`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `その他の詳細`, `カテゴリ表示順`, `キャンペーン`, `コラボスデータ`, `コーナン_加盟金あり` ... và 187 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`


---
## 完工予測 (Page 929628649)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| Store Example Data | `1cd1946f-e23...` | 5 |
| コラボス＋リペイント | `d767503e-113...` | 380 |
| コラボス＋リペイント（日別集計） | `72959d7c-7be...` | 32 |

**Tổng card KPI:** 16 | **Sẽ KHÔNG phản ứng với một số filter:** 16 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 前期 完工粗利進捗（完工・未完工集計） (Card 430670634)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/430670634)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 坂本あテスト＿  完工粗利進捗（完工・未完工集計） (Card 761208411)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/761208411)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 月別実績集計表（昨対比較含む） (Card 1175704747)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1175704747)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 前期 数字進捗集計（案件・見積・契約） (Card 800198233)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/800198233)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 完工粗利進捗（完工・未完工集計） (Card 476260492)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/476260492)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 前期 月別実績集計表（昨対比較含む) (Card 1183799360)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1183799360)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 数字進捗集計（案件・見積・契約） (Card 203300921)
- **Dataset:** コラボス＋リペイント（日別集計）
- **Columns có:** 32 | **Thiếu:** 246 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/203300921)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名` ... và 221 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 契約予定物件一覧（※フィルタはかかりません） (Card 917263084)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/917263084)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 今期 平均工事粗利 (Card 67574147)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/67574147)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 前期 平均工事粗利 (Card 958787017)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/958787017)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 工事粗利進捗（完工：確定分、未完工：完了予定日で集計） (Card 1962254929)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1962254929)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 前期 平均契約金額 (Card 1518625291)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1518625291)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 完工物件一覧（完工確認済み、支払い基準日入力物件） (Card 255857016)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/255857016)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 未完工物件一覧（工事完了予定日で抽出） (Card 2071676063)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/2071676063)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 今期 平均契約金額 (Card 1584937308)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1584937308)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`

#### 🔴 プロテック手数料予実（完工粗利予測） (Card 1918456637)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1918456637)**
- **Columns thiếu (từ dataset khác):**
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **コラボス＋リペイント（日別集計）**: `カテゴリ_変換`, `予実不足分`, `予実不足分（注力）`, `予算`, `契約実績`, `完工/未完工`, `実績`, `昨対比`, `昨年実績`, `期`, `注力予算`, `達成率`, `達成率（注力）`


---
## プロテック案件実績 (Page 1134665337)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| Store Example Data | `1cd1946f-e23...` | 5 |
| コラボス＋リペイント | `d767503e-113...` | 380 |
| コラボス＋リペイント（昨対集計用） | `6c6260a1-763...` | 11 |
| 積算チーム遵守率 | `2ab0037e-601...` | 14 |

**Tổng card KPI:** 20 | **Sẽ KHÔNG phản ứng với một số filter:** 20 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 コラボス_元請会社別新規案件数（昨対比）. (Card 131473852)
- **Dataset:** コラボス＋リペイント（昨対集計用）
- **Columns có:** 11 | **Thiếu:** 258 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/131473852)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 224 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `元請名`, `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問予定日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 島忠_累計新規案件数 (Card 691225406)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/691225406)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 DCM_累計新規案件数 (Card 491639767)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/491639767)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_DCM新規案件数（コラボス） (Card 400199465)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/400199465)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_一建設新規案件数（コラボス） (Card 382663062)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/382663062)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 一建設_累計新規案件数 (Card 1234487589)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1234487589)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 コラボス_累計新規案件数 (Card 1252179431)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1252179431)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 コーナン_累計新規案件数 (Card 1254719814)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1254719814)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 関西電力_累計新規案件数 (Card 1094235989)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1094235989)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_ヤマダデンキ新規案件数（コラボス） (Card 431395086)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/431395086)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 ヤマダデンキ_累計新規案件数 (Card 1560170550)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1560170550)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_コーナン新規案件数（コラボス） (Card 620429819)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/620429819)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_新規案件数（コラボス） (Card 2133931667)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/2133931667)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_アイリスプラザ新規案件数（コラボス） (Card 2060477552)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/2060477552)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 コラボス_元請け別新規案件数 (Card 1517610841)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1517610841)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 月次_新規案件数（コラボス） (Card 222570016)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/222570016)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 アイリスプラザ_累計新規案件数 (Card 25999181)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/25999181)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 案件一覧 (Card 1039323943)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1039323943)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_島忠新規案件数（コラボス） (Card 1322336018)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1322336018)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`

#### 🔴 週次_関西電力新規案件数（コラボス） (Card 1483605998)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 18 / 267
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1483605998)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント（昨対集計用）**: `date`, `昨年集計値`, `集計値`, `集計値の昨対比`
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`
  - Từ **積算チーム遵守率**: `判定`, `営業日数`, `対応件数`, `対象件数`, `翌営業日`, `見積提出日`, `訪問月`, `遵守率`, `顧客名`


---
## アパマン売上分析 (Page 1206453601)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| ER_売上/受注_直近_PRD | `d7d0cd1d-121...` | 887 |
| 【大型出荷有無用】ER_売上/受注_直近_PRD | `fa32aa9b-882...` | 25 |

**Tổng card KPI:** 13 | **Sẽ KHÔNG phản ứng với một số filter:** 13 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 月別_アパマン出荷社数 (Card 1037821389)
- **Dataset:** 【大型出荷有無用】ER_売上/受注_直近_PRD
- **Columns có:** 25 | **Thiếu:** 542 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1037821389)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `AP/PT種別区分`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)` ... và 522 columns khác

#### 🔴 出荷済社数_アパマン (Card 222412946)
- **Dataset:** 【大型出荷有無用】ER_売上/受注_直近_PRD
- **Columns có:** 25 | **Thiếu:** 542 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/222412946)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `AP/PT種別区分`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)` ... và 522 columns khác

#### 🔴 商品別_アパマン出荷現場数 (Card 1228599687)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1228599687)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_アパマン出荷現場数 (Card 1098878064)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1098878064)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_アパマン出荷現場数_年比較 (Card 1653484524)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1653484524)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_アパマン出荷_平均単価 (Card 36646733)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/36646733)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_アパマン売上 (Card 1538070797)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1538070797)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_アパマン売上_年比較 (Card 23606368)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/23606368)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 材料別_アパマン売上 (Card 1200401997)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1200401997)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_アパマン出荷社数_年比較 (Card 1515399157)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1515399157)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 ステータス別_ アパマン 出荷_平均単価_年比較 (Card 975517784)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/975517784)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 商品別_アパマン出荷社数 (Card 551221377)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/551221377)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`

#### 🔴 商品別_アパマン出荷_平均単価 (Card 753260540)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 4 / 561
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/753260540)**
- **Columns thiếu (từ dataset khác):**
  - Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**: `全社数`, `出荷フラグ`, `出荷済み社数`, `建物種別名（工場施設統合）`


---
## 商談未確定・郵送件数検索 (Page 1281028522)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| Store Example Data | `1cd1946f-e23...` | 5 |
| コラボス＋リペイント | `d767503e-113...` | 380 |

> ✅ Tất cả cards dùng cùng dataset. Không có vấn đề Filter Views cross-dataset.


---
## 商談・現調案件検索 (Page 1377736771)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| コラボス＋リペイント | `d767503e-113...` | 380 |

> ✅ Tất cả cards dùng cùng dataset. Không có vấn đề Filter Views cross-dataset.


---
## コラボス集計 (Page 1428843185)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| コラボス_契約率移動平均用 | `97b86f0a-3e0...` | 21 |
| コラボス集計 | `44fe3735-2fb...` | 118 |
| コラボス＋リペイント | `d767503e-113...` | 380 |

**Tổng card KPI:** 36 | **Sẽ KHÔNG phản ứng với một số filter:** 36 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 契約率（3ヶ月移動平均/60万円以上） (Card 988197674)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 257 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/988197674)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác
  - Từ **コラボス集計**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `キャンペーン`, `ステータス` ... và 79 columns khác

#### 🔴 契約率（12ヶ月移動平均） (Card 532453145)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 257 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/532453145)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác
  - Từ **コラボス集計**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `キャンペーン`, `ステータス` ... và 79 columns khác

#### 🔴 契約率（3ヶ月移動平均） (Card 1866181173)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 257 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1866181173)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác
  - Từ **コラボス集計**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `キャンペーン`, `ステータス` ... và 79 columns khác

#### 🔴 契約率（12ヶ月移動平均/60万円以上） (Card 909334434)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 257 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/909334434)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác
  - Từ **コラボス集計**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `キャンペーン`, `ステータス` ... và 79 columns khác

#### 🔴 見積提出数_グラフ（見積提案日基準） (Card 1887804995)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1887804995)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 見積提出数_60万以上_グラフ（見積提案日基準） (Card 164598919)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/164598919)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約金額_グラフ（結果確定日基準） (Card 17212857)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/17212857)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約金額 (Card 1492756894)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1492756894)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工数_グラフ（工事完了日基準） (Card 779700125)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/779700125)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約数_60万以上 (Card 1889903978)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1889903978)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工数_60万以上 (Card 691201626)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/691201626)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 見積提案数 (Card 1532260531)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1532260531)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工金額_60万以上_グラフ（工事完了日基準） (Card 1966591176)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1966591176)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 案件数_60万以上 (Card 1718162296)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1718162296)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約金額_60万以上 (Card 2075585989)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/2075585989)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工数_60万以上_グラフ（工事完了日基準） (Card 1754595176)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1754595176)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 案件数 (Card 41490049)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/41490049)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約数_グラフ（結果確定日基準） (Card 531776962)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/531776962)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 工事粗利_60万以上 (Card 1048755699)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1048755699)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 見積提案数_60万以上 (Card 1520589725)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1520589725)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工金額 (Card 1768862313)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1768862313)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 工事粗利_グラフ（支払基準日基準） (Card 1868388949)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1868388949)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 工事粗利_60万以上_グラフ（支払基準日基準） (Card 821020907)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/821020907)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約率（見積提案日基準・60万以上） (Card 82040535)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/82040535)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 案件数_60万以上_グラフ (Card 1653813382)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1653813382)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工金額_グラフ（工事完了日基準） (Card 1546556308)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1546556308)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工金額_60万以上 (Card 1573144144)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1573144144)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 工事粗利 (Card 894907839)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/894907839)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 案件発生数_グラフ（承り日基準） (Card 1952258545)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1952258545)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約率（見積提案日基準） (Card 1192997370)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1192997370)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約率_グラフ（見積提案日基準・60万以上） (Card 308637114)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/308637114)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約金額__60万以上 グラフ（結果確定日基準） (Card 379469956)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/379469956)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約数 (Card 1596693498)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1596693498)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約率_グラフ（見積提案日基準） (Card 1010684648)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1010684648)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工数 (Card 1813675019)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1813675019)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約数_60万以上_グラフ（結果確定日基準） (Card 1846390561)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 25 / 274
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1846390561)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`


---
## プロテックチームのキーエンス指標 (Page 1774230854)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| Zoho統合データ | `01b6c4e7-181...` | 287 |

> ✅ Tất cả cards dùng cùng dataset. Không có vấn đề Filter Views cross-dataset.


---
## 全体管理 (Page 1827358914)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| ER_受注/出荷_直近_PRD | `cec7172d-098...` | 421 |
| ER_売上/受注_直近_PRD | `d7d0cd1d-121...` | 887 |
| コラボス_契約率移動平均用 | `97b86f0a-3e0...` | 21 |
| コラボス＋リペイント | `d767503e-113...` | 380 |

**Tổng card KPI:** 47 | **Sẽ KHÔNG phản ứng với một số filter:** 47 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 契約率（3ヶ月移動平均） (Card 1866181173)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 852 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1866181173)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `AP/PT種別区分`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)` ... và 537 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `AP/PT種別区分`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(受注時)` ... và 301 columns khác
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác

#### 🔴 契約率（3ヶ月移動平均/60万円以上） (Card 988197674)
- **Dataset:** コラボス_契約率移動平均用
- **Columns có:** 21 | **Thiếu:** 852 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/988197674)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `AP/PT種別区分`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)` ... và 537 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `AP/PT種別区分`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(受注時)` ... và 301 columns khác
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `company_id`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year` ... và 223 columns khác

#### 🔴 他社塗料購入粗利 (Card 1302356523)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1302356523)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 完工件数 (Card 1802584313)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1802584313)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 紹介モデル手数料 (Card 417208681)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/417208681)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 契約件数 (Card 1881220917)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1881220917)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場塗料粗利_グラフ (Card 583145161)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/583145161)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 アパマン_塗料粗利 (Card 643073117)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/643073117)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 契約件数_グラフ (Card 1551637113)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1551637113)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 カイゼンReペイント＆工場アパマン手数料 予実 (Card 747665703)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/747665703)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 契約率（見積提案日基準・60万以上） (Card 82040535)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/82040535)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_塗料粗利予実表_当月 (Card 991329451)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/991329451)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 沖縄_塗料注文件数_グラフ (Card 1307059860)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1307059860)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_塗料粗利 予実 (Card 742909363)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/742909363)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 大規模修繕 (Card 381801388)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/381801388)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工事粗利_グラフ (Card 703377110)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/703377110)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 プロテック塗料粗利 (Card 1519241531)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1519241531)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場・アパマン塗料粗利_グラフ (Card 1540274693)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1540274693)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場アパマン成約手数料_グラフ (Card 264124591)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/264124591)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 プロテック塗料注文件数 (Card 1757213491)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1757213491)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 大規模修繕注文件数_グラフ (Card 2090189264)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/2090189264)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場アパマン紹介手数料 (Card 612296022)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/612296022)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 プロテック手数料 予実 (Card 1108873039)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1108873039)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_手数料予実_当月 (Card 1607768844)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1607768844)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_塗料粗利 予実 (Card 798110155)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/798110155)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場・アパマン_塗料粗利 (Card 119774191)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/119774191)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_塗料粗利 予実 (Card 1140052288)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1140052288)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 沖縄_塗料粗利 (Card 908199668)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/908199668)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工事粗利 (Card 1417532884)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1417532884)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 プロテック塗料粗利 (Card 1562411866)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1562411866)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場・アパマン塗料注文件数_グラフ (Card 198091187)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/198091187)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場アパマン紹介手数料_グラフ (Card 223021489)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/223021489)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 アパマン塗料注文件数_グラフ (Card 199640344)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/199640344)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 CAD作成代行費用（プロテック） (Card 1897760483)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1897760483)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場塗料注文件数_グラフ (Card 282162621)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/282162621)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場_塗料粗利 (Card 870418362)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/870418362)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 完工件数_グラフ (Card 144862465)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/144862465)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 契約率（見積提案日基準） (Card 1192997370)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1192997370)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_全体予実 (Card 1635302702)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1635302702)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 大規模修繕粗利_グラフ (Card 1013435713)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1013435713)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 施工店登録費用 (Card 671546784)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/671546784)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 法人営業部_塗料粗利 予実（経理確認用） (Card 325383362)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/325383362)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 工場アパマン成約手数料 (Card 1480269791)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1480269791)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 沖縄_塗料粗利_グラフ (Card 814591635)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/814591635)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 アパマン塗料粗利_グラフ (Card 1455082981)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 620 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1455082981)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS商品フラグ`, `APS（2%）プロタイムズ専用`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ` ... và 498 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `APS商品フラグ`, `AP_Reカバーチーム名`, `APチームID`, `APチームID(実績担当基準)`, `APチーム名`, `APチーム名(実績担当基準)`, `APユニットID`, `APユニットID(実績担当基準)`, `APユニット名`, `APユニット名(実績担当基準)`, `APリーダーフラグ`, `APリーダーフラグ(実績担当基準)`, `AP営業所ID`, `AP営業所ID(受注時)`, `AP営業所ID(実績担当基準)`, `AP営業所名`, `AP営業所名(実績担当基準)`, `AP担当者ID` ... và 268 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`

#### 🔴 商品別売上（カイゼンReペイント） (Card 1092187899)
- **Dataset:** ER_受注/出荷_直近_PRD
- **Columns có:** 421 | **Thiếu:** 548 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1092187899)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID`, `PT売上予算`, `PT売上予算累計` ... và 307 columns khác
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `元請会社`, `元請会社（DCMまとめ）`, `営業担当`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `担当センター`, `担当施工店`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`, `都道府県`
  - Từ **コラボス＋リペイント**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `SCチャネル`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `その他`, `その他の詳細` ... và 196 columns khác

#### 🔴 商品別売上（カイゼンReペイント）_グラフ (Card 308568308)
- **Dataset:** ER_売上/受注_直近_PRD
- **Columns có:** 887 | **Thiếu:** 312 / 869
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/308568308)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス_契約率移動平均用**: `60万円以上`, `今日まで`, `元請会社`, `元請会社（DCMまとめ）`, `営業担当`, `契約率集計用年`, `契約率集計用日付`, `契約率集計用月`, `契約率（3ヶ月移動平均）`, `平均期間`, `担当センター`, `担当施工店`, `日付軸`, `月別契約件数`, `月別見積件数`, `結果/見積`, `都道府県`
  - Từ **コラボス＋リペイント**: `Budget_Type`, `Budget_date`, `Date`, `Days of month`, `Holyday_Amount_Zero`, `Month`, `_BATCH_FILE_ID_`, `_BATCH_FILE_NAME_`, `_BATCH_ID_`, `_BATCH_LAST_RUN_`, `_BATCH_ROW_NUM_`, `calendar_date`, `sales_office_id`, `sales_office_name`, `salesuser_id`, `year`, `お客様氏名`, `その他`, `その他の詳細`, `カテゴリ` ... và 190 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `GT集計用カテゴリ名`, `OEM先伝達事項`, `WEB切替_WEB受注率`, `WEB切替_ポテンシャル`, `WEB切替_受注件数(APO)`, `WEB切替_受注件数(CS)`, `WEB切替_受注件数(NAVI)`, `WEB切替_受注件数(営業)`, `WEB切替_受注経路区分=「受注以外」除外`, `WEB切替_注文合計`, `WEB切替_顧客会社アステック除外`, `Web受注率`, `Web受注率ジャンプ`, `Web受注率用経路表示順`, `アステック加盟年`, `カイゼンReペイント（NULL・空削除）`, `チャレンジカップ用商品名`, `上塗缶数合計`, `会計勘定科目`, `出荷.出荷ID` ... và 71 columns khác


---
## 週間MTG用コラボス分析 (Page 1959758463)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| コラボス集計 | `44fe3735-2fb...` | 118 |
| コラボス＋リペイント | `d767503e-113...` | 380 |

**Tổng card KPI:** 16 | **Sẽ KHÔNG phản ứng với một số filter:** 16 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 【期待値込】プロテック請負金額集計_元請別（計上予定日基準） (Card 1255037399)
- **Dataset:** コラボス集計
- **Columns có:** 118 | **Thiếu:** 159 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1255037399)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス＋リペイント**: `AP/PT種別区分`, `AP営業所名(受注時)`, `SCチャネル`, `その他`, `その他の詳細`, `カテゴリ`, `カテゴリ表示順`, `コラボスデータ`, `コーナン_加盟金あり`, `コーナン_加盟金なし`, `スポットチェンジ判断`, `データ元`, `プロテック販促品`, `ポイント値引き`, `ユニット`, `ユニット(並び替え用)`, `ユニット表示`, `予算種類`, `事業所`, `事業所表示順` ... và 139 columns khác

#### 🔴 見積予実_元請別 (Card 587114568)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/587114568)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 平均見積金額_元請別(直近1年間) (Card 44262708)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/44262708)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 平均日数_施工店別 (Card 1861520957)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1861520957)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約予実_元請別 (Card 460265818)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/460265818)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工予実_元請別 (Card 570077680)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/570077680)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 施工店請負金額_施工店別（工事完了日基準） (Card 1376120614)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1376120614)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 現調数_施工店別（訪問日基準） (Card 370751928)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/370751928)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約予実_担当別 (Card 1787571010)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1787571010)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 対応案件数_施工店別（見積提案日基準） (Card 821964464)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/821964464)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 契約数_施工店別（結果確定日基準） (Card 25377069)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/25377069)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 見積予実_担当別 (Card 1037568660)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1037568660)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工予実_元請別（注力外） (Card 496855862)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/496855862)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 完工予実_担当別 (Card 526521217)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/526521217)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 平均見積金額_元請別(直近3ヶ月) (Card 1704425485)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1704425485)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`

#### 🔴 プロテック請負金額集計_担当別 (Card 1171272019)
- **Dataset:** コラボス＋リペイント
- **Columns có:** 380 | **Thiếu:** 15 / 264
- **[Xem card](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1171272019)**
- **Columns thiếu (từ dataset khác):**
  - Từ **コラボス集計**: `ステータス`, `プロテック請負金額（合計）`, `契約件数（3ヶ月移動平均・60万以上）`, `契約件数（3ヶ月移動平均）`, `契約率（3ヶ月移動平均・60万円以上）`, `契約率（3ヶ月移動平均）`, `実績判断`, `平均契約金額`, `手数料確度`, `期待値の計上日`, `検討中案件数`, `確度用ステージ`, `見積①提出数`, `見積提案件数（3ヶ月移動平均・60万以上）`, `見積提案件数（3ヶ月移動平均）`


---
## 法人営業部用_売上集計(出荷日基準) (Page 2006619322)

### Datasets trên page

| Dataset | ID | Columns |
|:---|:---|:---:|
| ER_受注/出荷_直近_PRD | `cec7172d-098...` | 421 |
| ER_売上/受注_直近_PRD | `d7d0cd1d-121...` | 887 |
| ER_現場名入り受注 | `44eb7b46-09d...` | 319 |
| Store Example Data | `1cd1946f-e23...` | 5 |

**Tổng card KPI:** 4 | **Sẽ KHÔNG phản ứng với một số filter:** 4 | **Đầy đủ:** 0

### Cards không phản ứng với một số Filter Views

#### 🔴 Duplicate of 次の複製： 売上詳細(出荷日基準) (Card 289460039)
- **Dataset:** ER_現場名入り受注
- **Columns có:** 319 | **Thiếu:** 415 / 703
- **[Xem card](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/289460039)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `#粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID` ... và 338 columns khác
  - Từ **ER_受注/出荷_直近_PRD**: `#粗利率`, `APS`, `GT集計用カテゴリ名`, `WEB切替_WEB受注率`, `WEB切替_ポテンシャル`, `WEB切替_受注件数(APO)`, `WEB切替_受注件数(CS)`, `WEB切替_受注件数(NAVI)`, `WEB切替_受注件数(営業)`, `WEB切替_受注経路区分=「受注以外」除外`, `WEB切替_注文合計`, `WEB切替_顧客会社アステック除外`, `Web受注率`, `Web受注率ジャンプ`, `Web受注率用経路表示順`, `アステック加盟年`, `カイゼンReペイント（NULL・空削除）`, `チャレンジカップ用商品名`, `プロタイムズ加盟種別`, `プロタイムズ注文除外` ... và 63 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 Duplicate of 次の複製： 売上集計表(出荷日基準) (Card 260858484)
- **Dataset:** ER_受注/出荷_直近_PRD
- **Columns có:** 421 | **Thiếu:** 382 / 703
- **[Xem card](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/260858484)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID`, `PT売上予算`, `PT売上予算累計` ... và 307 columns khác
  - Từ **ER_現場名入り受注**: `ER_現場名(制限あり)._BATCH_ID_`, `ER_現場名(制限あり)._BATCH_LAST_RUN_`, `ER_現場名(制限あり).company_id`, `ER_現場名(制限あり).note`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `office_id`, `pref_cd`, `pref_nm`, `prime_contractor_name` ... và 30 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 Duplicate of 次の複製： 売上実績(出荷日基準) (Card 1258504332)
- **Dataset:** ER_受注/出荷_直近_PRD
- **Columns có:** 421 | **Thiếu:** 382 / 703
- **[Xem card](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/1258504332)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID`, `PT売上予算`, `PT売上予算累計` ... và 307 columns khác
  - Từ **ER_現場名入り受注**: `ER_現場名(制限あり)._BATCH_ID_`, `ER_現場名(制限あり)._BATCH_LAST_RUN_`, `ER_現場名(制限あり).company_id`, `ER_現場名(制限あり).note`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `office_id`, `pref_cd`, `pref_nm`, `prime_contractor_name` ... và 30 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

#### 🔴 Duplicate of 売上集計表 (Card 948537816)
- **Dataset:** ER_受注/出荷_直近_PRD
- **Columns có:** 421 | **Thiếu:** 382 / 703
- **[Xem card](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/948537816)**
- **Columns thiếu (từ dataset khác):**
  - Từ **ER_売上/受注_直近_PRD**: ` CMS用新規カテゴリ表示順`, `#売上年`, `#目標粗利率`, `2026年_おうちReカバー_条件`, `38期Reカバーチーム`, `APS以外（8.5%）プロタイムズ専用`, `APS（2%）プロタイムズ専用`, `AP営業所名表示順`, `AP営業所名（受注時）表示順`, `AP担当者ID（0消し）`, `AP担当者名 (表示順)`, `CMS_加盟店材料別_塗料の表示順`, `CMS_加盟店材料別_塗料カテゴリ`, `CMS_加盟店材料別_塗料カテゴリ表示順`, `CMS用カテゴリ`, `CMS用新規カテゴリ`, `GV商品`, `ID`, `PT売上予算`, `PT売上予算累計` ... và 307 columns khác
  - Từ **ER_現場名入り受注**: `ER_現場名(制限あり)._BATCH_ID_`, `ER_現場名(制限あり)._BATCH_LAST_RUN_`, `ER_現場名(制限あり).company_id`, `ER_現場名(制限あり).note`, `block_buildings_nm`, `building_type`, `city_nm`, `contact_address_tel01`, `contact_address_tel02`, `contact_address_tel03`, `customer_id`, `first_order_date`, `logical_delete_flag`, `mobile_phone_number01`, `mobile_phone_number02`, `mobile_phone_number03`, `office_id`, `pref_cd`, `pref_nm`, `prime_contractor_name` ... và 30 columns khác
  - Từ **Store Example Data**: `date_ymd`, `department`, `revenue`, `sales_rep`, `state`

