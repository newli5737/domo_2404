# DOMO Filter Views Audit Report v2

Phân tích Filter Views với phân loại **FORMULA** (beastmode, có thể tạo lại) vs **COLUMN** (physical, không thể thêm).

> **Ký hiệu:**
> - 🟡 **FORMULA (Beastmode)** — Column này là công thức tính toán. Có thể tạo formula tương tự trong dataset đích.
> - 🔵 **COLUMN (Physical)** — Column vật lý chỉ tồn tại trong dataset nguồn. Không thể thêm vào dataset khác.

## Tổng quan

| Page | Page Title | Datasets | Cards | Thiếu Formula | Thiếu Physical |
|:---|:---|:---:|:---:|:---:|:---:|
| 193413623 | 工場アパマンチームのキーエンス指標 | 1 | 6 | 0 | 0 |
| 213860614 | 施工店分析 | 3 | 25 | 612 | 707 |
| 248150074 | 工場売上分析 | 3 | 14 | 1125 | 972 |
| 836254252 | 物件種別修正用 | 4 | 3 | 1201 | 417 |
| 929628649 | 完工予測 | 3 | 16 | 970 | 914 |
| 1134665337 | プロテック案件実績 | 4 | 20 | 209 | 391 |
| 1206453601 | アパマン売上分析 | 2 | 13 | 678 | 450 |
| 1281028522 | 商談未確定・郵送件数検索 | 2 | 18 | 0 | 90 |
| 1377736771 | 商談・現調案件検索 | 1 | 20 | 0 | 0 |
| 1428843185 | コラボス集計 | 3 | 36 | 796 | 1032 |
| 1774230854 | プロテックチームのキーエンス指標 | 1 | 6 | 0 | 0 |
| 1827358914 | 全体管理 | 4 | 47 | 17904 | 11320 |
| 1959758463 | 週間MTG用コラボス分析 | 2 | 16 | 213 | 171 |
| 2006619322 | 法人営業部用_売上集計(出荷日基準) | 4 | 4 | 1272 | 289 |


---
## 工場アパマンチームのキーエンス指標 (Page 193413623)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| Zoho統合データ | 113 | 174 |

> ✅ Chỉ 1 dataset. Không có vấn đề cross-dataset.


---
## 施工店分析 (Page 213860614)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| コラボス_契約率移動平均用 | 13 | 8 |
| コラボス＋リペイント | 118 | 262 |
| コラボス＋リペイント（昨対集計用） | 7 | 4 |

### Cards dùng dataset: **コラボス＋リペイント**

**21 cards** bị ảnh hưởng:
- 未完工一覧 (Card 633141134) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/633141134)
- 契約一覧(見積結果日基準) (Card 1931412914) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1931412914)
- 平均単価(施工店請負金額) (Card 1851405345) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1851405345)
- 商談未確定率（見積提案日基準） (Card 1969287996) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1969287996)
- 月別施工店ごと商談未確定件数(今期) (Card 138189276) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/138189276)
- 見積数（見積提案日基準） (Card 53616018) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/53616018)
- 契約数(結果確定日基準) (Card 710284790) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/710284790)
- 案件一覧(施工店用_承り日基準) (Card 1465358268) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1465358268)
- 完工一覧（工事完了予定日基準） (Card 2147160344) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/2147160344)
- 案件数（承り日基準） (Card 395356149) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/395356149)
- 平均日数（施工店別） (Card 595232334) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/595232334)
- 郵送率（施工店でフィルター必須） (Card 831102014) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/831102014)
- 郵送率（3ヶ月毎） (Card 1288974591) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1288974591)
- 見積件数一覧(見積提案日基準) (Card 765442322) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/765442322)
- 元請け別契約金額(結果確定日基準) (Card 1579225174) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1579225174)
- 契約率(施工店分析） (Card 90992398) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/90992398)
- 完工一覧 (Card 1123284518) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1123284518)
- 月別施工店ごと郵送件数(今期) (Card 868287800) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/868287800)
- 元請け別完工金額 (Card 1715340574) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1715340574)
- 商談未確定率（3ヶ月毎） (Card 1137777881) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1137777881)
- 契約率_グラフ（見積提案日基準） (Card 1010684648) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1010684648)

#### 🟡 Missing Formulas (Beastmodes) — 4 columns — *có thể tạo lại*

Từ **コラボス_契約率移動平均用**:
- `今日まで`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

Từ **コラボス＋リペイント（昨対集計用）**:
- `集計値の昨対比`

#### 🔵 Missing Physical Columns — 11 columns — *không thể thêm*

Từ **コラボス_契約率移動平均用**:
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`

Từ **コラボス＋リペイント（昨対集計用）**:
- `date`
- `昨年集計値`
- `集計値`

### Cards dùng dataset: **コラボス_契約率移動平均用**

**2 cards** bị ảnh hưởng:
- 契約率（12ヶ月移動平均） (Card 532453145) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/532453145)
- 契約率（3ヶ月移動平均） (Card 1866181173) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/1866181173)

#### 🟡 Missing Formulas (Beastmodes) — 131 columns — *có thể tạo lại*

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- ... và 100 beastmodes khác

Từ **コラボス＋リペイント（昨対集計用）**:
- `カテゴリ表示順`
- `集計値の昨対比`

#### 🔵 Missing Physical Columns — 116 columns — *không thể thêm*

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `カテゴリ`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- ... và 83 physical columns khác

Từ **コラボス＋リペイント（昨対集計用）**:
- `date`
- `カテゴリ`
- `昨年集計値`
- `集計値`

### Cards dùng dataset: **コラボス＋リペイント（昨対集計用）**

**2 cards** bị ảnh hưởng:
- 数値進捗（施工店）3ヶ月集計 (Card 206632515) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/206632515)
- 数値進捗（施工店） (Card 118066549) — [Link](https://astecpaints-co-jp.domo.com/page/213860614/kpis/details/118066549)

#### 🟡 Missing Formulas (Beastmodes) — 133 columns — *có thể tạo lại*

Từ **コラボス＋リペイント**:
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- ... và 100 beastmodes khác

Từ **コラボス_契約率移動平均用**:
- `今日まで`
- `元請会社（DCMまとめ）`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

#### 🔵 Missing Physical Columns — 122 columns — *không thể thêm*

Từ **コラボス_契約率移動平均用**:
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `担当センター`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`
- `都道府県`

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- ... và 84 physical columns khác


---
## 工場売上分析 (Page 248150074)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| ER_売上/受注_直近_PRD | 227 | 660 |
| ER_現場名入り売上実績 | 267 | 50 |
| 【大型出荷有無用】ER_売上/受注_直近_PRD | 13 | 12 |

### Cards dùng dataset: **ER_売上/受注_直近_PRD**

**11 cards** bị ảnh hưởng:
- ステータス別_工場・倉庫・施設出荷社数_年比較 (Card 228624032) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/228624032)
- 商品別_工場・倉庫・施設出荷現場数 (Card 674045266) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/674045266)
- ステータス別_工場・倉庫・施設売上 (Card 1924842861) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1924842861)
- 商品別_工場・倉庫・施設出荷社数 (Card 1341591185) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1341591185)
- ステータス別_工場・倉庫・施設出荷現場数 (Card 572002633) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/572002633)
- ステータス別_工場・倉庫・施設出荷_平均単価_年比較 (Card 571321567) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/571321567)
- ステータス別_工場・倉庫・施設売上_年比較 (Card 1712590684) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1712590684)
- ステータス別_工場・倉庫・施設出荷現場数_年比較 (Card 335358071) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/335358071)
- 商品別_工場・倉庫・施設出荷_平均単価 (Card 988661802) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/988661802)
- ステータス別_工場・倉庫・施設出荷_平均単価 (Card 1491562448) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1491562448)
- 材料別_工場・倉庫・施設売上 (Card 647931224) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/647931224)

#### 🟡 Missing Formulas (Beastmodes) — 12 columns — *có thể tạo lại*

Từ **ER_現場名入り売上実績**:
- `CX出荷社数`
- `CX加盟店出荷社数`
- `SC元請出荷社数`
- `カテゴリ`
- `コーナン（加盟金あり）名`
- `コーナン（加盟金なし）名`
- `売上額/現場数`
- `新規キャンペーン用売上額`
- `施工店グループ（その他）`
- `粗利額/現場数`

Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**:
- `全社数`
- `出荷済み社数`

#### 🔵 Missing Physical Columns — 42 columns — *không thể thêm*

Từ **ER_現場名入り売上実績**:
- `ER_現場名(制限あり).company_id`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `block_buildings_nm`
- `building_type`
- `city_nm`
- `contact_address_tel01`
- `contact_address_tel02`
- `contact_address_tel03`
- `customer_id`
- `first_order_date`
- `logical_delete_flag`
- `mobile_phone_number01`
- `mobile_phone_number02`
- `mobile_phone_number03`
- `note`
- `office_id`
- `pref_cd`
- `pref_nm`
- `prime_contractor_name`
- `property_type`
- `regist_datetime`
- `regist_user_id`
- `register_source_type`
- `shipping_kana01`
- `shipping_kana02`
- `shipping_nm01`
- `shipping_nm02`
- `site_id`
- `site_zipcode`
- ... và 10 physical columns khác

Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**:
- `出荷フラグ`
- `建物種別名（工場施設統合）`

### Cards dùng dataset: **【大型出荷有無用】ER_売上/受注_直近_PRD**

**2 cards** bị ảnh hưởng:
- 月別_工場・倉庫・施設出荷社数 (Card 1017947390) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1017947390)
- 出荷済社数_工場・施設 (Card 1734810736) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1734810736)

#### 🟡 Missing Formulas (Beastmodes) — 338 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 298 beastmodes khác

Từ **ER_現場名入り売上実績**:
- `CX出荷社数`
- `CX加盟店出荷社数`
- `SC元請出荷社数`
- `カテゴリ`
- `コーナン（加盟金あり）名`
- `コーナン（加盟金なし）名`
- `ポイント値引き`
- `勘定科目`
- `半期`
- `受注ステータス仮保存除外`
- `商品荷姿艶`
- `塗料系統`
- `売上年月（〇年△月）`
- `売上額`
- `売上額/現場数`
- `新規キャンペーン用売上額`
- `施工店グループ（その他）`
- `無償提供`
- `特別値引き`
- `現場ポケット売上`
- `現場数`
- `粗利額`
- `粗利額/現場数`
- `規格/塗料色`
- `請求グループ`

#### 🔵 Missing Physical Columns — 254 columns — *không thể thêm*

Từ **ER_売上/受注_直近_PRD**:
- `AP/PT種別区分`
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名(受注時)`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名(受注時)`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- `PT事業所ID`
- `PT事業所ID(受注時)`
- `PT事業所名`
- ... và 184 physical columns khác

Từ **ER_現場名入り売上実績**:
- `AP/PT種別区分`
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名(受注時)`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名(受注時)`
- `ER_現場名(制限あり).company_id`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- `PT事業所ID`
- `PT事業所ID(受注時)`
- ... và 224 physical columns khác

### Cards dùng dataset: **ER_現場名入り売上実績**

**1 cards** bị ảnh hưởng:
- 工場案件一覧 (Card 1643529095) — [Link](https://astecpaints-co-jp.domo.com/page/248150074/kpis/details/1643529095)

#### 🟡 Missing Formulas (Beastmodes) — 317 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 285 beastmodes khác

Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**:
- `全社数`
- `出荷済み社数`
- `加盟店子ランク表示順`
- `売上時期`

#### 🔵 Missing Physical Columns — 2 columns — *không thể thêm*

Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**:
- `出荷フラグ`
- `建物種別名（工場施設統合）`


---
## 物件種別修正用 (Page 836254252)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| ER_売上/受注_直近_PRD | 227 | 660 |
| ER_現場名入り売上実績 | 267 | 50 |
| Store Example Data | 5 | 0 |
| コラボス＋リペイント | 118 | 262 |

### Cards dùng dataset: **ER_現場名入り売上実績**

**2 cards** bị ảnh hưởng:
- ERAWAN_物件種別(すべて) (Card 916494563) — [Link](https://astecpaints-co-jp.domo.com/page/836254252/kpis/details/916494563)
- 物件種別修正用一覧_ERAWAN (Card 1675340749) — [Link](https://astecpaints-co-jp.domo.com/page/836254252/kpis/details/1675340749)

#### 🟡 Missing Formulas (Beastmodes) — 436 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 285 beastmodes khác

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- `契約金額平均(直近1年分)`
- `契約金額平均(直近3ヶ月)`
- `契約金額達成率`
- ... và 93 beastmodes khác

#### 🔵 Missing Physical Columns — 89 columns — *không thể thêm*

Từ **コラボス＋リペイント**:
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他の詳細`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- `会社名`
- `住所`
- `元請け担当者`
- `元請会社`
- `商品券(金額)`
- `営業担当`
- `売上区分`
- ... và 54 physical columns khác

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

### Cards dùng dataset: **コラボス＋リペイント**

**1 cards** bị ảnh hưởng:
- 物件種別修正用一覧_コラボス (Card 936888329) — [Link](https://astecpaints-co-jp.domo.com/page/836254252/kpis/details/936888329)

#### 🟡 Missing Formulas (Beastmodes) — 329 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 290 beastmodes khác

Từ **ER_現場名入り売上実績**:
- `CX出荷社数`
- `CX加盟店出荷社数`
- `SC元請出荷社数`
- `コーナン（加盟金あり）名`
- `コーナン（加盟金なし）名`
- `半期`
- `受注ステータス仮保存除外`
- `商品荷姿艶`
- `塗料系統`
- `売上年月（〇年△月）`
- `売上額/現場数`
- `新規キャンペーン用売上額`
- `施工店グループ（その他）`
- `現場数`
- `粗利額/現場数`
- `規格/塗料色`

#### 🔵 Missing Physical Columns — 239 columns — *không thể thêm*

Từ **ER_売上/受注_直近_PRD**:
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名`
- `AP担当者名(受注時)`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- `PT事業所ID`
- ... và 168 physical columns khác

Từ **ER_現場名入り売上実績**:
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名`
- `AP担当者名(受注時)`
- `ER_現場名(制限あり).company_id`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- ... và 204 physical columns khác

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`


---
## 完工予測 (Page 929628649)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| Store Example Data | 5 | 0 |
| コラボス＋リペイント | 118 | 262 |
| コラボス＋リペイント（日別集計） | 10 | 22 |

### Cards dùng dataset: **コラボス＋リペイント（日別集計）**

**7 cards** bị ảnh hưởng:
- 前期 完工粗利進捗（完工・未完工集計） (Card 430670634) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/430670634)
- 坂本あテスト＿  完工粗利進捗（完工・未完工集計） (Card 761208411) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/761208411)
- 月別実績集計表（昨対比較含む） (Card 1175704747) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1175704747)
- 前期 数字進捗集計（案件・見積・契約） (Card 800198233) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/800198233)
- 完工粗利進捗（完工・未完工集計） (Card 476260492) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/476260492)
- 前期 月別実績集計表（昨対比較含む) (Card 1183799360) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1183799360)
- 数字進捗集計（案件・見積・契約） (Card 203300921) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/203300921)

#### 🟡 Missing Formulas (Beastmodes) — 127 columns — *có thể tạo lại*

Từ **コラボス＋リペイント**:
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `売上日`
- `売上月`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- `契約金額平均(直近1年分)`
- `契約金額平均(直近3ヶ月)`
- `契約金額達成率`
- ... và 97 beastmodes khác

#### 🔵 Missing Physical Columns — 119 columns — *không thể thêm*

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `Budget_Type`
- `Budget_date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- `予算種類`
- ... và 84 physical columns khác

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

### Cards dùng dataset: **コラボス＋リペイント**

**9 cards** bị ảnh hưởng:
- 契約予定物件一覧（※フィルタはかかりません） (Card 917263084) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/917263084)
- 今期 平均工事粗利 (Card 67574147) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/67574147)
- 前期 平均工事粗利 (Card 958787017) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/958787017)
- 工事粗利進捗（完工：確定分、未完工：完了予定日で集計） (Card 1962254929) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1962254929)
- 前期 平均契約金額 (Card 1518625291) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1518625291)
- 完工物件一覧（完工確認済み、支払い基準日入力物件） (Card 255857016) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/255857016)
- 未完工物件一覧（工事完了予定日で抽出） (Card 2071676063) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/2071676063)
- 今期 平均契約金額 (Card 1584937308) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1584937308)
- プロテック手数料予実（完工粗利予測） (Card 1918456637) — [Link](https://astecpaints-co-jp.domo.com/page/929628649/kpis/details/1918456637)

#### 🟡 Missing Formulas (Beastmodes) — 9 columns — *có thể tạo lại*

Từ **コラボス＋リペイント（日別集計）**:
- `カテゴリ_変換`
- `予実不足分`
- `予実不足分（注力）`
- `契約実績`
- `昨対比`
- `期`
- `注力予算`
- `達成率`
- `達成率（注力）`

#### 🔵 Missing Physical Columns — 9 columns — *không thể thêm*

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

Từ **コラボス＋リペイント（日別集計）**:
- `予算`
- `完工/未完工`
- `実績`
- `昨年実績`


---
## プロテック案件実績 (Page 1134665337)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| Store Example Data | 5 | 0 |
| コラボス＋リペイント | 118 | 262 |
| コラボス＋リペイント（昨対集計用） | 7 | 4 |
| 積算チーム遵守率 | 8 | 6 |

### Cards dùng dataset: **コラボス＋リペイント**

**19 cards** bị ảnh hưởng:
- 島忠_累計新規案件数 (Card 691225406) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/691225406)
- DCM_累計新規案件数 (Card 491639767) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/491639767)
- 週次_DCM新規案件数（コラボス） (Card 400199465) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/400199465)
- 週次_一建設新規案件数（コラボス） (Card 382663062) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/382663062)
- 一建設_累計新規案件数 (Card 1234487589) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1234487589)
- コラボス_累計新規案件数 (Card 1252179431) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1252179431)
- コーナン_累計新規案件数 (Card 1254719814) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1254719814)
- 関西電力_累計新規案件数 (Card 1094235989) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1094235989)
- 週次_ヤマダデンキ新規案件数（コラボス） (Card 431395086) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/431395086)
- ヤマダデンキ_累計新規案件数 (Card 1560170550) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1560170550)
- 週次_コーナン新規案件数（コラボス） (Card 620429819) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/620429819)
- 週次_新規案件数（コラボス） (Card 2133931667) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/2133931667)
- 週次_アイリスプラザ新規案件数（コラボス） (Card 2060477552) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/2060477552)
- コラボス_元請け別新規案件数 (Card 1517610841) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1517610841)
- 月次_新規案件数（コラボス） (Card 222570016) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/222570016)
- アイリスプラザ_累計新規案件数 (Card 25999181) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/25999181)
- 案件一覧 (Card 1039323943) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1039323943)
- 週次_島忠新規案件数（コラボス） (Card 1322336018) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1322336018)
- 週次_関西電力新規案件数（コラボス） (Card 1483605998) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/1483605998)

#### 🟡 Missing Formulas (Beastmodes) — 4 columns — *có thể tạo lại*

Từ **積算チーム遵守率**:
- `対応件数`
- `対象件数`
- `遵守率`

Từ **コラボス＋リペイント（昨対集計用）**:
- `集計値の昨対比`

#### 🔵 Missing Physical Columns — 14 columns — *không thể thêm*

Từ **コラボス＋リペイント（昨対集計用）**:
- `date`
- `昨年集計値`
- `集計値`

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

Từ **積算チーム遵守率**:
- `判定`
- `営業日数`
- `翌営業日`
- `見積提出日`
- `訪問月`
- `顧客名`

### Cards dùng dataset: **コラボス＋リペイント（昨対集計用）**

**1 cards** bị ảnh hưởng:
- コラボス_元請会社別新規案件数（昨対比）. (Card 131473852) — [Link](https://astecpaints-co-jp.domo.com/page/1134665337/kpis/details/131473852)

#### 🟡 Missing Formulas (Beastmodes) — 133 columns — *có thể tạo lại*

Từ **コラボス＋リペイント**:
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- ... và 100 beastmodes khác

Từ **積算チーム遵守率**:
- `元請名`
- `対応件数`
- `対象件数`
- `遵守率`

#### 🔵 Missing Physical Columns — 125 columns — *không thể thêm*

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- ... và 84 physical columns khác

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

Từ **積算チーム遵守率**:
- `判定`
- `営業日数`
- `翌営業日`
- `見積提出日`
- `訪問予定日`
- `訪問月`
- `顧客名`


---
## アパマン売上分析 (Page 1206453601)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| ER_売上/受注_直近_PRD | 227 | 660 |
| 【大型出荷有無用】ER_売上/受注_直近_PRD | 13 | 12 |

### Cards dùng dataset: **ER_売上/受注_直近_PRD**

**11 cards** bị ảnh hưởng:
- 商品別_アパマン出荷現場数 (Card 1228599687) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1228599687)
- ステータス別_アパマン出荷現場数 (Card 1098878064) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1098878064)
- ステータス別_アパマン出荷現場数_年比較 (Card 1653484524) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1653484524)
- ステータス別_アパマン出荷_平均単価 (Card 36646733) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/36646733)
- ステータス別_アパマン売上 (Card 1538070797) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1538070797)
- ステータス別_アパマン売上_年比較 (Card 23606368) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/23606368)
- 材料別_アパマン売上 (Card 1200401997) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1200401997)
- ステータス別_アパマン出荷社数_年比較 (Card 1515399157) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1515399157)
- ステータス別_ アパマン 出荷_平均単価_年比較 (Card 975517784) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/975517784)
- 商品別_アパマン出荷社数 (Card 551221377) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/551221377)
- 商品別_アパマン出荷_平均単価 (Card 753260540) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/753260540)

#### 🟡 Missing Formulas (Beastmodes) — 2 columns — *có thể tạo lại*

Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**:
- `全社数`
- `出荷済み社数`

#### 🔵 Missing Physical Columns — 2 columns — *không thể thêm*

Từ **【大型出荷有無用】ER_売上/受注_直近_PRD**:
- `出荷フラグ`
- `建物種別名（工場施設統合）`

### Cards dùng dataset: **【大型出荷有無用】ER_売上/受注_直近_PRD**

**2 cards** bị ảnh hưởng:
- 月別_アパマン出荷社数 (Card 1037821389) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/1037821389)
- 出荷済社数_アパマン (Card 222412946) — [Link](https://astecpaints-co-jp.domo.com/page/1206453601/kpis/details/222412946)

#### 🟡 Missing Formulas (Beastmodes) — 328 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 298 beastmodes khác

#### 🔵 Missing Physical Columns — 214 columns — *không thể thêm*

Từ **ER_売上/受注_直近_PRD**:
- `AP/PT種別区分`
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名(受注時)`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名(受注時)`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- `PT事業所ID`
- `PT事業所ID(受注時)`
- `PT事業所名`
- ... và 184 physical columns khác


---
## 商談未確定・郵送件数検索 (Page 1281028522)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| Store Example Data | 5 | 0 |
| コラボス＋リペイント | 118 | 262 |

### Cards dùng dataset: **コラボス＋リペイント**

**18 cards** bị ảnh hưởng:
- 月別元請けごと郵送件数(前期) (Card 501835661) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/501835661)
- その他元請別商談未確定件数(見積提案日基準) (Card 745437269) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/745437269)
- 郵送未確定率(今月) (Card 793217449) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/793217449)
- 月別元請けごと商談未確定件数(今期) (Card 1458968856) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1458968856)
- 商談未確定率(見積提案日基準) (Card 1851052092) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1851052092)
- 郵送案件一覧(見積提案日基準) (Card 849120903) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/849120903)
- 月別施工店ごと郵送件数(今期) (Card 868287800) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/868287800)
- 注力元請別商談未確定件数(見積提案日基準) (Card 375432919) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/375432919)
- 月別施工店ごと郵送件数(前期) (Card 1274644734) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1274644734)
- 郵送合計件数(見積提案日基準) (Card 1392125953) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1392125953)
- 注力元請別郵送件数(今月) (Card 1148770875) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1148770875)
- 月別元請けごと商談未確定案件数(前期) (Card 1409183744) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1409183744)
- 月別元請けごと郵送件数(今期) (Card 999361246) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/999361246)
- 商談日未確定案件一覧(見積提案日基準) (Card 719910242) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/719910242)
- 月別施工店ごと商談未確定件数(前期) (Card 2144385797) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/2144385797)
- その他元請別郵送件数(今月) (Card 1669657755) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/1669657755)
- 商談未確定案件数(見積提案日基準) (Card 390114331) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/390114331)
- 月別施工店ごと商談未確定件数(今期) (Card 138189276) — [Link](https://astecpaints-co-jp.domo.com/page/1281028522/kpis/details/138189276)

#### 🔵 Missing Physical Columns — 5 columns — *không thể thêm*

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`


---
## 商談・現調案件検索 (Page 1377736771)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| コラボス＋リペイント | 118 | 262 |

> ✅ Chỉ 1 dataset. Không có vấn đề cross-dataset.


---
## コラボス集計 (Page 1428843185)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| コラボス_契約率移動平均用 | 13 | 8 |
| コラボス集計 | 92 | 26 |
| コラボス＋リペイント | 118 | 262 |

### Cards dùng dataset: **コラボス＋リペイント**

**32 cards** bị ảnh hưởng:
- 見積提出数_グラフ（見積提案日基準） (Card 1887804995) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1887804995)
- 見積提出数_60万以上_グラフ（見積提案日基準） (Card 164598919) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/164598919)
- 契約金額_グラフ（結果確定日基準） (Card 17212857) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/17212857)
- 契約金額 (Card 1492756894) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1492756894)
- 完工数_グラフ（工事完了日基準） (Card 779700125) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/779700125)
- 契約数_60万以上 (Card 1889903978) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1889903978)
- 完工数_60万以上 (Card 691201626) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/691201626)
- 見積提案数 (Card 1532260531) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1532260531)
- 完工金額_60万以上_グラフ（工事完了日基準） (Card 1966591176) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1966591176)
- 案件数_60万以上 (Card 1718162296) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1718162296)
- 契約金額_60万以上 (Card 2075585989) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/2075585989)
- 完工数_60万以上_グラフ（工事完了日基準） (Card 1754595176) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1754595176)
- 案件数 (Card 41490049) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/41490049)
- 契約数_グラフ（結果確定日基準） (Card 531776962) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/531776962)
- 工事粗利_60万以上 (Card 1048755699) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1048755699)
- 見積提案数_60万以上 (Card 1520589725) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1520589725)
- 完工金額 (Card 1768862313) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1768862313)
- 工事粗利_グラフ（支払基準日基準） (Card 1868388949) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1868388949)
- 工事粗利_60万以上_グラフ（支払基準日基準） (Card 821020907) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/821020907)
- 契約率（見積提案日基準・60万以上） (Card 82040535) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/82040535)
- 案件数_60万以上_グラフ (Card 1653813382) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1653813382)
- 完工金額_グラフ（工事完了日基準） (Card 1546556308) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1546556308)
- 完工金額_60万以上 (Card 1573144144) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1573144144)
- 工事粗利 (Card 894907839) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/894907839)
- 案件発生数_グラフ（承り日基準） (Card 1952258545) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1952258545)
- 契約率（見積提案日基準） (Card 1192997370) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1192997370)
- 契約率_グラフ（見積提案日基準・60万以上） (Card 308637114) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/308637114)
- 契約金額__60万以上 グラフ（結果確定日基準） (Card 379469956) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/379469956)
- 契約数 (Card 1596693498) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1596693498)
- 契約率_グラフ（見積提案日基準） (Card 1010684648) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1010684648)
- 完工数 (Card 1813675019) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1813675019)
- 契約数_60万以上_グラフ（結果確定日基準） (Card 1846390561) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1846390561)

#### 🟡 Missing Formulas (Beastmodes) — 8 columns — *có thể tạo lại*

Từ **コラボス集計**:
- `プロテック請負金額（合計）`
- `契約率（3ヶ月移動平均・60万円以上）`
- `契約率（3ヶ月移動平均）`
- `平均契約金額`
- `検討中案件数`
- `見積①提出数`

Từ **コラボス_契約率移動平均用**:
- `今日まで`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

#### 🔵 Missing Physical Columns — 17 columns — *không thể thêm*

Từ **コラボス_契約率移動平均用**:
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`

Từ **コラボス集計**:
- `ステータス`
- `契約件数（3ヶ月移動平均・60万以上）`
- `契約件数（3ヶ月移動平均）`
- `実績判断`
- `手数料確度`
- `期待値の計上日`
- `確度用ステージ`
- `見積提案件数（3ヶ月移動平均・60万以上）`
- `見積提案件数（3ヶ月移動平均）`

### Cards dùng dataset: **コラボス_契約率移動平均用**

**4 cards** bị ảnh hưởng:
- 契約率（3ヶ月移動平均/60万円以上） (Card 988197674) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/988197674)
- 契約率（12ヶ月移動平均） (Card 532453145) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/532453145)
- 契約率（3ヶ月移動平均） (Card 1866181173) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/1866181173)
- 契約率（12ヶ月移動平均/60万円以上） (Card 909334434) — [Link](https://astecpaints-co-jp.domo.com/page/1428843185/kpis/details/909334434)

#### 🟡 Missing Formulas (Beastmodes) — 135 columns — *có thể tạo lại*

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- ... và 100 beastmodes khác

Từ **コラボス集計**:
- `プロテック請負金額（合計）`
- `契約件数`
- `契約件数達成率`
- `契約率`
- `契約率（3ヶ月移動平均・60万円以上）`
- `契約金額達成率`
- `完工粗利予算（注力）`
- `工事粗利`
- `平均契約金額`
- `検討中案件数`
- `見積①提出数`
- `見積提案年`
- `見積提案月`

#### 🔵 Missing Physical Columns — 122 columns — *không thể thêm*

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `カテゴリ`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- ... và 83 physical columns khác

Từ **コラボス集計**:
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `キャンペーン`
- `ステータス`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- `住所`
- `元請け担当者`
- `商品券(金額)`
- `売上区分`
- `契約件数予算_Per_Day`
- `契約件数予算（個人）_Per_Day`
- `契約件数（3ヶ月移動平均・60万以上）`
- ... và 56 physical columns khác


---
## プロテックチームのキーエンス指標 (Page 1774230854)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| Zoho統合データ | 113 | 174 |

> ✅ Chỉ 1 dataset. Không có vấn đề cross-dataset.


---
## 全体管理 (Page 1827358914)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| ER_受注/出荷_直近_PRD | 221 | 200 |
| ER_売上/受注_直近_PRD | 227 | 660 |
| コラボス_契約率移動平均用 | 13 | 8 |
| コラボス＋リペイント | 118 | 262 |

### Cards dùng dataset: **コラボス＋リペイント**

**43 cards** bị ảnh hưởng:
- 他社塗料購入粗利 (Card 1302356523) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1302356523)
- 完工件数 (Card 1802584313) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1802584313)
- 紹介モデル手数料 (Card 417208681) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/417208681)
- 契約件数 (Card 1881220917) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1881220917)
- 工場塗料粗利_グラフ (Card 583145161) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/583145161)
- アパマン_塗料粗利 (Card 643073117) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/643073117)
- 契約件数_グラフ (Card 1551637113) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1551637113)
- カイゼンReペイント＆工場アパマン手数料 予実 (Card 747665703) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/747665703)
- 契約率（見積提案日基準・60万以上） (Card 82040535) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/82040535)
- 法人営業部_塗料粗利予実表_当月 (Card 991329451) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/991329451)
- 沖縄_塗料注文件数_グラフ (Card 1307059860) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1307059860)
- 法人営業部_塗料粗利 予実 (Card 742909363) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/742909363)
- 大規模修繕 (Card 381801388) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/381801388)
- 工事粗利_グラフ (Card 703377110) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/703377110)
- プロテック塗料粗利 (Card 1519241531) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1519241531)
- 工場・アパマン塗料粗利_グラフ (Card 1540274693) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1540274693)
- 工場アパマン成約手数料_グラフ (Card 264124591) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/264124591)
- プロテック塗料注文件数 (Card 1757213491) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1757213491)
- 大規模修繕注文件数_グラフ (Card 2090189264) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/2090189264)
- 工場アパマン紹介手数料 (Card 612296022) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/612296022)
- プロテック手数料 予実 (Card 1108873039) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1108873039)
- 法人営業部_手数料予実_当月 (Card 1607768844) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1607768844)
- 法人営業部_塗料粗利 予実 (Card 798110155) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/798110155)
- 工場・アパマン_塗料粗利 (Card 119774191) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/119774191)
- 法人営業部_塗料粗利 予実 (Card 1140052288) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1140052288)
- 沖縄_塗料粗利 (Card 908199668) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/908199668)
- 工事粗利 (Card 1417532884) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1417532884)
- プロテック塗料粗利 (Card 1562411866) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1562411866)
- 工場・アパマン塗料注文件数_グラフ (Card 198091187) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/198091187)
- 工場アパマン紹介手数料_グラフ (Card 223021489) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/223021489)
- アパマン塗料注文件数_グラフ (Card 199640344) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/199640344)
- CAD作成代行費用（プロテック） (Card 1897760483) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1897760483)
- 工場塗料注文件数_グラフ (Card 282162621) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/282162621)
- 工場_塗料粗利 (Card 870418362) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/870418362)
- 完工件数_グラフ (Card 144862465) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/144862465)
- 契約率（見積提案日基準） (Card 1192997370) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1192997370)
- 法人営業部_全体予実 (Card 1635302702) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1635302702)
- 大規模修繕粗利_グラフ (Card 1013435713) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1013435713)
- 施工店登録費用 (Card 671546784) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/671546784)
- 法人営業部_塗料粗利 予実（経理確認用） (Card 325383362) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/325383362)
- 工場アパマン成約手数料 (Card 1480269791) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1480269791)
- 沖縄_塗料粗利_グラフ (Card 814591635) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/814591635)
- アパマン塗料粗利_グラフ (Card 1455082981) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1455082981)

#### 🟡 Missing Formulas (Beastmodes) — 379 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 291 beastmodes khác

Từ **ER_受注/出荷_直近_PRD**:
- `#粗利率`
- `APS`
- `GT集計用カテゴリ名`
- `WEB切替_WEB受注率`
- `WEB切替_ポテンシャル`
- `WEB切替_受注件数(APO)`
- `WEB切替_受注件数(CS)`
- `WEB切替_受注件数(NAVI)`
- `WEB切替_受注件数(営業)`
- `WEB切替_受注経路区分=「受注以外」除外`
- `WEB切替_注文合計`
- `WEB切替_顧客会社アステック除外`
- `Web受注率`
- `Web受注率ジャンプ`
- `Web受注率用経路表示順`
- `アステック加盟年`
- `アステック加盟種別`
- `カイゼンReペイント（NULL・空削除）`
- `カイゼンリペイント`
- `チャレンジカップ用商品名`
- `プロタイムズ加盟種別`
- `プロタイムズ注文除外`
- `上塗缶数合計`
- `会計勘定科目`
- `出荷.出荷依頼先名表示順`
- `出荷ステータス名`
- `出荷年月`
- `出荷日（表示用）`
- `出荷済受注`
- `分類名（リファイン_屋根壁分割）`
- ... và 60 beastmodes khác

Từ **コラボス_契約率移動平均用**:
- `今日まで`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

#### 🔵 Missing Physical Columns — 241 columns — *không thể thêm*

Từ **コラボス_契約率移動平均用**:
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`

Từ **ER_受注/出荷_直近_PRD**:
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名`
- `AP担当者名(受注時)`
- `OEM先伝達事項`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- ... và 168 physical columns khác

Từ **ER_売上/受注_直近_PRD**:
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名`
- `AP担当者名(受注時)`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- `PT予算額`
- `PT事業所ID`
- ... và 167 physical columns khác

### Cards dùng dataset: **ER_売上/受注_直近_PRD**

**1 cards** bị ảnh hưởng:
- 商品別売上（カイゼンReペイント）_グラフ (Card 308568308) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/308568308)

#### 🟡 Missing Formulas (Beastmodes) — 179 columns — *có thể tạo lại*

Từ **ER_受注/出荷_直近_PRD**:
- `GT集計用カテゴリ名`
- `WEB切替_WEB受注率`
- `WEB切替_ポテンシャル`
- `WEB切替_受注件数(APO)`
- `WEB切替_受注件数(CS)`
- `WEB切替_受注件数(NAVI)`
- `WEB切替_受注件数(営業)`
- `WEB切替_受注経路区分=「受注以外」除外`
- `WEB切替_注文合計`
- `WEB切替_顧客会社アステック除外`
- `Web受注率`
- `Web受注率ジャンプ`
- `Web受注率用経路表示順`
- `アステック加盟年`
- `カイゼンReペイント（NULL・空削除）`
- `チャレンジカップ用商品名`
- `上塗缶数合計`
- `会計勘定科目`
- `出荷.出荷依頼先名表示順`
- `出荷ステータス名`
- `出荷年月`
- `出荷日（表示用）`
- `加盟グループ_プロテック（フィラー2Ⅱ含）`
- `受注ステータス（受注簡易システム）`
- `受注合計(受注単位)`
- `受注年`
- `受注年月`
- `受注日`
- `受注経路区分名称`
- `受注経路区分名称(Webデバイス込み)`
- ... và 25 beastmodes khác

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- `契約金額平均(直近1年分)`
- `契約金額平均(直近3ヶ月)`
- `契約金額達成率`
- ... và 91 beastmodes khác

Từ **コラボス_契約率移動平均用**:
- `今日まで`
- `元請会社（DCMまとめ）`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

#### 🔵 Missing Physical Columns — 133 columns — *không thể thêm*

Từ **コラボス_契約率移動平均用**:
- `60万円以上`
- `元請会社`
- `営業担当`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `担当センター`
- `担当施工店`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`
- `都道府県`

Từ **コラボス＋リペイント**:
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `カテゴリ`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- `会社ID`
- `会社名`
- `住所`
- ... và 59 physical columns khác

Từ **ER_受注/出荷_直近_PRD**:
- `OEM先伝達事項`
- `出荷.出荷ID`
- `出荷.出荷ステータス`
- `出荷.出荷依頼先ID`
- `出荷.出荷依頼先名`
- `出荷.出荷依頼日時`
- `出荷.出荷明細ID`
- `出荷.納期日`
- `出荷.送り状番号`
- `出荷.配送業者ID`
- `出荷年`
- `出荷日`
- `出荷月`
- `加盟グループ_SCチャネル`
- `加盟グループ_アステック`
- `加盟グループ_プロタイムズ`
- `加盟グループ_プロテック`
- `加盟グループ_プロテック（フィラーⅡ）`
- `加盟チャネル_工場アパマン`
- `受付担当者ID`
- `受注チェック担当者ID`
- `番地・建物名`
- `直近受注`
- `納品先携帯番号１`
- `納品先携帯番号２`
- `納品先携帯番号３`
- `納品先電話番号１`
- `納品先電話番号２`
- `納品先電話番号３`
- `納品希望日`
- ... và 6 physical columns khác

### Cards dùng dataset: **コラボス_契約率移動平均用**

**2 cards** bị ảnh hưởng:
- 契約率（3ヶ月移動平均） (Card 1866181173) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1866181173)
- 契約率（3ヶ月移動平均/60万円以上） (Card 988197674) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/988197674)

#### 🟡 Missing Formulas (Beastmodes) — 508 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 303 beastmodes khác

Từ **ER_受注/出荷_直近_PRD**:
- `#粗利率`
- `APS`
- `GT集計用カテゴリ名`
- `WEB切替_WEB受注率`
- `WEB切替_ポテンシャル`
- `WEB切替_受注件数(APO)`
- `WEB切替_受注件数(CS)`
- `WEB切替_受注件数(NAVI)`
- `WEB切替_受注件数(営業)`
- `WEB切替_受注経路区分=「受注以外」除外`
- `WEB切替_注文合計`
- `WEB切替_顧客会社アステック除外`
- `Web受注率`
- `Web受注率ジャンプ`
- `Web受注率用経路表示順`
- `アステック加盟年`
- `アステック加盟種別`
- `カイゼンReペイント（NULL・空削除）`
- `カイゼンリペイント`
- `チャレンジカップ用商品名`
- `プロタイムズ加盟種別`
- `プロタイムズ注文除外`
- `ポイント値引き`
- `上塗缶数合計`
- `会計勘定科目`
- `出荷.出荷依頼先名表示順`
- `出荷ステータス名`
- `出荷年月`
- `出荷日（表示用）`
- `出荷済受注`
- ... và 70 beastmodes khác

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `売上額`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- ... và 102 beastmodes khác

#### 🔵 Missing Physical Columns — 344 columns — *không thể thêm*

Từ **ER_受注/出荷_直近_PRD**:
- `AP/PT種別区分`
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名`
- `AP営業所名(受注時)`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名`
- `AP担当者名(受注時)`
- `OEM先伝達事項`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- ... và 191 physical columns khác

Từ **ER_売上/受注_直近_PRD**:
- `AP/PT種別区分`
- `APS商品フラグ`
- `AP_Reカバーチーム名`
- `APチームID`
- `APチームID(実績担当基準)`
- `APチーム名`
- `APチーム名(実績担当基準)`
- `APユニットID`
- `APユニットID(実績担当基準)`
- `APユニット名`
- `APユニット名(実績担当基準)`
- `APリーダーフラグ`
- `APリーダーフラグ(実績担当基準)`
- `AP営業所ID`
- `AP営業所ID(受注時)`
- `AP営業所ID(実績担当基準)`
- `AP営業所名`
- `AP営業所名(受注時)`
- `AP営業所名(実績担当基準)`
- `AP担当者ID`
- `AP担当者ID(受注時)`
- `AP担当者名`
- `AP担当者名(受注時)`
- `PB会社ID`
- `PB会社ID(受注時)`
- `PB営業所ID`
- `PB店舗ID`
- `PB店舗名`
- `PTのSVID`
- `PT予算月目標`
- ... và 194 physical columns khác

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `company_id`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `カテゴリ`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- ... và 81 physical columns khác

### Cards dùng dataset: **ER_受注/出荷_直近_PRD**

**1 cards** bị ảnh hưởng:
- 商品別売上（カイゼンReペイント） (Card 1092187899) — [Link](https://astecpaints-co-jp.domo.com/page/1827358914/kpis/details/1092187899)

#### 🟡 Missing Formulas (Beastmodes) — 412 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- `PT手数料累計`
- `PT手数料累計（24年~14%Ver）`
- ... và 258 beastmodes khác

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `契約件数`
- `契約件数(結果確定日基準)`
- `契約件数達成率`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約率`
- `契約金額平均(直近1年分)`
- ... và 93 beastmodes khác

Từ **コラボス_契約率移動平均用**:
- `今日まで`
- `元請会社（DCMまとめ）`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

#### 🔵 Missing Physical Columns — 136 columns — *không thể thêm*

Từ **コラボス_契約率移動平均用**:
- `60万円以上`
- `元請会社`
- `営業担当`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `担当センター`
- `担当施工店`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`
- `都道府県`

Từ **コラボス＋リペイント**:
- `Budget_Type`
- `Budget_date`
- `Date`
- `Days of month`
- `Holyday_Amount_Zero`
- `Month`
- `SCチャネル`
- `_BATCH_FILE_ID_`
- `_BATCH_FILE_NAME_`
- `_BATCH_ID_`
- `_BATCH_LAST_RUN_`
- `_BATCH_ROW_NUM_`
- `calendar_date`
- `sales_office_id`
- `sales_office_name`
- `salesuser_id`
- `year`
- `お客様氏名`
- `その他`
- `その他の詳細`
- `カテゴリ`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `フリガナ`
- `プロテックセンター 受付日`
- `プロテック請負金額`
- `会社ID`
- `会社名`
- ... và 63 physical columns khác

Từ **ER_売上/受注_直近_PRD**:
- `SCチャネル`
- `アステック`
- `ステージ（商談）`
- `プロタイムズ`
- `プロテック`
- `プロテック（フィラーⅡ）`
- `下請け工事の塗料選定割合`
- `受注区分（加盟1年以内）`
- `受注区分（立上げ対象）`
- `営業日フラグ`
- `営業日数(年月)`
- `営業日数(期)`
- `塗装売上（下請け）（取引先）`
- `塗装売上（元請け）（取引先）`
- `売上.会社ID`
- `売上.出荷ID`
- `売上.勘定科目名`
- `売上.単価`
- `売上.受注詳細ID`
- `売上.商品ID`
- `売上.商品コード`
- `売上.商品名`
- `売上.売上ID`
- `売上.所属営業所ID`
- `売上.数量`
- `売上年`
- `売上年月最大日`
- `売上日最大`
- `大型切り替えキャンペーン`
- `工場アパマン`
- ... và 9 physical columns khác


---
## 週間MTG用コラボス分析 (Page 1959758463)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| コラボス集計 | 92 | 26 |
| コラボス＋リペイント | 118 | 262 |

### Cards dùng dataset: **コラボス集計**

**1 cards** bị ảnh hưởng:
- 【期待値込】プロテック請負金額集計_元請別（計上予定日基準） (Card 1255037399) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1255037399)

#### 🟡 Missing Formulas (Beastmodes) — 123 columns — *có thể tạo lại*

Từ **コラボス＋リペイント**:
- `カテゴリ表示順`
- `コラボスデータ`
- `スポットチェンジ判断`
- `プロテック販促品`
- `ポイント値引き`
- `ユニット`
- `ユニット(並び替え用)`
- `ユニット表示`
- `事業所`
- `事業所表示順`
- `元請け表示順`
- `元請会社(すぽっとチェンジ)`
- `元請会社(表示修正)`
- `元請会社（DCMまとめ）`
- `元請名`
- `元請名ソート`
- `全体_予算達成率`
- `利益率`
- `勘定科目`
- `商談予定件数`
- `営業担当（文字化け修正）`
- `売上日`
- `売上月`
- `契約件数(結果確定日基準)`
- `契約件数達成率_個人`
- `契約件数（60万以上）`
- `契約年`
- `契約月`
- `契約金額平均(直近1年分)`
- `契約金額平均(直近3ヶ月)`
- ... và 93 beastmodes khác

#### 🔵 Missing Physical Columns — 36 columns — *không thể thêm*

Từ **コラボス＋リペイント**:
- `AP/PT種別区分`
- `AP営業所名(受注時)`
- `SCチャネル`
- `その他`
- `その他の詳細`
- `カテゴリ`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- `データ元`
- `予算種類`
- `会社ID`
- `会社名`
- `加盟チャネル名`
- `勘定科目としての種別`
- `単価`
- `原価`
- `受注ID`
- `受注詳細ID`
- `商品名`
- `商品種別`
- `商材.原価率`
- `売上.単価`
- `売上.商品コード`
- `売上.数量`
- `売上額`
- `建物区分名`
- `承り日（土曜〜週次集計用）`
- `無償提供フラグ`
- `物件種別`
- `物件種別名`
- ... và 6 physical columns khác

### Cards dùng dataset: **コラボス＋リペイント**

**15 cards** bị ảnh hưởng:
- 見積予実_元請別 (Card 587114568) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/587114568)
- 平均見積金額_元請別(直近1年間) (Card 44262708) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/44262708)
- 平均日数_施工店別 (Card 1861520957) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1861520957)
- 契約予実_元請別 (Card 460265818) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/460265818)
- 完工予実_元請別 (Card 570077680) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/570077680)
- 施工店請負金額_施工店別（工事完了日基準） (Card 1376120614) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1376120614)
- 現調数_施工店別（訪問日基準） (Card 370751928) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/370751928)
- 契約予実_担当別 (Card 1787571010) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1787571010)
- 対応案件数_施工店別（見積提案日基準） (Card 821964464) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/821964464)
- 契約数_施工店別（結果確定日基準） (Card 25377069) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/25377069)
- 見積予実_担当別 (Card 1037568660) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1037568660)
- 完工予実_元請別（注力外） (Card 496855862) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/496855862)
- 完工予実_担当別 (Card 526521217) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/526521217)
- 平均見積金額_元請別(直近3ヶ月) (Card 1704425485) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1704425485)
- プロテック請負金額集計_担当別 (Card 1171272019) — [Link](https://astecpaints-co-jp.domo.com/page/1959758463/kpis/details/1171272019)

#### 🟡 Missing Formulas (Beastmodes) — 6 columns — *có thể tạo lại*

Từ **コラボス集計**:
- `プロテック請負金額（合計）`
- `契約率（3ヶ月移動平均・60万円以上）`
- `契約率（3ヶ月移動平均）`
- `平均契約金額`
- `検討中案件数`
- `見積①提出数`

#### 🔵 Missing Physical Columns — 9 columns — *không thể thêm*

Từ **コラボス集計**:
- `ステータス`
- `契約件数（3ヶ月移動平均・60万以上）`
- `契約件数（3ヶ月移動平均）`
- `実績判断`
- `手数料確度`
- `期待値の計上日`
- `確度用ステージ`
- `見積提案件数（3ヶ月移動平均・60万以上）`
- `見積提案件数（3ヶ月移動平均）`


---
## 法人営業部用_売上集計(出荷日基準) (Page 2006619322)

### Datasets

| Dataset | Physical Cols | Beastmodes |
|:---|:---:|:---:|
| ER_受注/出荷_直近_PRD | 221 | 200 |
| ER_売上/受注_直近_PRD | 227 | 660 |
| ER_現場名入り受注 | 257 | 62 |
| Store Example Data | 5 | 0 |

### Cards dùng dataset: **ER_受注/出荷_直近_PRD**

**3 cards** bị ảnh hưởng:
- Duplicate of 次の複製： 売上集計表(出荷日基準) (Card 260858484) — [Link](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/260858484)
- Duplicate of 次の複製： 売上実績(出荷日基準) (Card 1258504332) — [Link](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/1258504332)
- Duplicate of 売上集計表 (Card 948537816) — [Link](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/948537816)

#### 🟡 Missing Formulas (Beastmodes) — 301 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- `PT手数料累計`
- `PT手数料累計（24年~14%Ver）`
- ... và 256 beastmodes khác

Từ **ER_現場名入り受注**:
- `おうちReカバー集計カテゴリ`
- `ポイント還元率名`
- `加盟店子ランク/価格ランク`
- `原価額`
- `受注ステータス名`
- `受注経路区分名`
- `売上金額`
- `売上額（計）`
- `携帯番号`
- `現場納品表示用`
- `納品時連絡名`
- `色番号 / 塗料名`
- `見やすい受注日時（時間込み）`
- `配送業者名`
- `電話番号`

#### 🔵 Missing Physical Columns — 81 columns — *không thể thêm*

Từ **ER_現場名入り受注**:
- `ER_現場名(制限あり)._BATCH_ID_`
- `ER_現場名(制限あり)._BATCH_LAST_RUN_`
- `ER_現場名(制限あり).company_id`
- `ER_現場名(制限あり).note`
- `block_buildings_nm`
- `building_type`
- `city_nm`
- `contact_address_tel01`
- `contact_address_tel02`
- `contact_address_tel03`
- `customer_id`
- `first_order_date`
- `logical_delete_flag`
- `mobile_phone_number01`
- `mobile_phone_number02`
- `mobile_phone_number03`
- `office_id`
- `pref_cd`
- `pref_nm`
- `prime_contractor_name`
- `property_type`
- `regist_datetime`
- `regist_user_id`
- `register_source_type`
- `shipping_kana01`
- `shipping_kana02`
- `shipping_nm01`
- `shipping_nm02`
- `site_id`
- `site_zipcode`
- ... và 5 physical columns khác

Từ **ER_売上/受注_直近_PRD**:
- `SCチャネル`
- `アステック`
- `ステージ（商談）`
- `プロタイムズ`
- `プロテック`
- `プロテック（フィラーⅡ）`
- `下請け工事の塗料選定割合`
- `受注区分（加盟1年以内）`
- `受注区分（立上げ対象）`
- `営業日フラグ`
- `営業日数(年月)`
- `営業日数(期)`
- `塗装売上（下請け）（取引先）`
- `塗装売上（元請け）（取引先）`
- `売上.会社ID`
- `売上.出荷ID`
- `売上.勘定科目名`
- `売上.単価`
- `売上.受注詳細ID`
- `売上.商品ID`
- `売上.商品コード`
- `売上.商品名`
- `売上.売上ID`
- `売上.所属営業所ID`
- `売上.数量`
- `売上年`
- `売上年月最大日`
- `売上日`
- `売上日最大`
- `売上月`
- ... và 11 physical columns khác

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

### Cards dùng dataset: **ER_現場名入り受注**

**1 cards** bị ảnh hưởng:
- Duplicate of 次の複製： 売上詳細(出荷日基準) (Card 289460039) — [Link](https://astecpaints-co-jp.domo.com/page/2006619322/kpis/details/289460039)

#### 🟡 Missing Formulas (Beastmodes) — 369 columns — *có thể tạo lại*

Từ **ER_売上/受注_直近_PRD**:
- ` CMS用新規カテゴリ表示順`
- `#売上年`
- `#目標粗利率`
- `#粗利率`
- `2026年_おうちReカバー_条件`
- `38期Reカバーチーム`
- `APS`
- `APS以外（8.5%）プロタイムズ専用`
- `APS（2%）プロタイムズ専用`
- `AP営業所名表示順`
- `AP営業所名（受注時）表示順`
- `AP担当者ID（0消し）`
- `AP担当者名 (表示順)`
- `CMS_加盟店材料別_塗料の表示順`
- `CMS_加盟店材料別_塗料カテゴリ`
- `CMS_加盟店材料別_塗料カテゴリ表示順`
- `CMS用カテゴリ`
- `CMS用新規カテゴリ`
- `GV商品`
- `ID`
- `PT売上予算`
- `PT売上予算累計`
- `PT売上予算達成率`
- `PT手数料`
- `PT手数料(平均予測)`
- `PT手数料(平均予測:月次)`
- `PT手数料(色分用)`
- `PT手数料予算(可変)`
- `PT手数料予算累計`
- `PT手数料目標達成率（24年~14%Ver）`
- ... và 287 beastmodes khác

Từ **ER_受注/出荷_直近_PRD**:
- `#粗利率`
- `APS`
- `GT集計用カテゴリ名`
- `WEB切替_WEB受注率`
- `WEB切替_ポテンシャル`
- `WEB切替_受注件数(APO)`
- `WEB切替_受注件数(CS)`
- `WEB切替_受注件数(NAVI)`
- `WEB切替_受注件数(営業)`
- `WEB切替_受注経路区分=「受注以外」除外`
- `WEB切替_注文合計`
- `WEB切替_顧客会社アステック除外`
- `Web受注率`
- `Web受注率ジャンプ`
- `Web受注率用経路表示順`
- `アステック加盟年`
- `カイゼンReペイント（NULL・空削除）`
- `チャレンジカップ用商品名`
- `プロタイムズ加盟種別`
- `プロタイムズ注文除外`
- `上塗缶数合計`
- `会計勘定科目`
- `出荷.出荷依頼先名表示順`
- `出荷日（表示用）`
- `出荷済受注`
- `分類名（リファイン_屋根壁分割）`
- `加盟グループ_プロテック（フィラー2Ⅱ含）`
- `半期`
- `受注ステータス（受注簡易システム）`
- `受注合計(受注単位)`
- ... và 53 beastmodes khác

#### 🔵 Missing Physical Columns — 46 columns — *không thể thêm*

Từ **ER_売上/受注_直近_PRD**:
- `SCチャネル`
- `アステック`
- `ステージ（商談）`
- `プロタイムズ`
- `プロテック`
- `プロテック（フィラーⅡ）`
- `下請け工事の塗料選定割合`
- `受注区分（加盟1年以内）`
- `受注区分（立上げ対象）`
- `営業日フラグ`
- `営業日数(年月)`
- `営業日数(期)`
- `塗装売上（下請け）（取引先）`
- `塗装売上（元請け）（取引先）`
- `売上.会社ID`
- `売上.出荷ID`
- `売上.勘定科目名`
- `売上.単価`
- `売上.受注詳細ID`
- `売上.商品ID`
- `売上.商品コード`
- `売上.商品名`
- `売上.売上ID`
- `売上.所属営業所ID`
- `売上.数量`
- `売上年`
- `売上年月最大日`
- `売上日`
- `売上日最大`
- `売上月`
- ... và 11 physical columns khác

Từ **Store Example Data**:
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

