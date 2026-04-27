# Beastmode Formula Reproducibility Analysis

Phân tích khả năng tạo lại các beastmode (formula) bị thiếu ở dataset đích.

> **Lưu ý:** HAR files KHÔNG chứa formula expressions (được lưu server-side bởi DOMO).
> Phân tích dựa trên **physical column overlap** giữa dataset nguồn và dataset đích.
> Overlap cao = khả năng formula dùng các column chung → có thể tạo lại.

> **Feasibility levels:**
> - 🟢 **HIGH** (≥80% overlap) — Hầu hết physical columns giống nhau → formula rất có thể tạo lại
> - 🟡 **MEDIUM** (50-80%) — Khá nhiều columns chung → có thể tạo lại một phần
> - 🟠 **LOW** (20-50%) — Ít columns chung → khó tạo lại
> - 🔴 **VERY LOW** (<20%) — Gần như không có column chung → không thể tạo lại


---
## 施工店分析 (Page 213860614)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| コラボス_契約率移動平均用 | 13 | 4 | 17 |
| コラボス＋リペイント | 118 | 131 | 249 |
| コラボス＋リペイント（昨対集計用） | 7 | 2 | 9 |

### Physical Column Overlap Matrix

| Target \ Source | コラボス_契約率移動平均用 | コラボス＋リペイント | コラボス＋リペイント（昨対集計用） |
|:---|:---:|:---:|:---:|
| コラボス_契約率移動平均用 | - | 🔴 4% (5/118) | 🟠 43% (3/7) |
| コラボス＋リペイント | 🟠 38% (5/13) | - | 🟡 57% (4/7) |
| コラボス＋リペイント（昨対集計用） | 🟠 23% (3/13) | 🔴 3% (4/118) | - |

### Cards dùng: **コラボス＋リペイント** (21 cards)

<details><summary>Danh sách cards</summary>

- 未完工一覧 (Card 633141134)
- 契約一覧(見積結果日基準) (Card 1931412914)
- 平均単価(施工店請負金額) (Card 1851405345)
- 商談未確定率（見積提案日基準） (Card 1969287996)
- 月別施工店ごと商談未確定件数(今期) (Card 138189276)
- 見積数（見積提案日基準） (Card 53616018)
- 契約数(結果確定日基準) (Card 710284790)
- 案件一覧(施工店用_承り日基準) (Card 1465358268)
- 完工一覧（工事完了予定日基準） (Card 2147160344)
- 案件数（承り日基準） (Card 395356149)
- 平均日数（施工店別） (Card 595232334)
- 郵送率（施工店でフィルター必須） (Card 831102014)
- 郵送率（3ヶ月毎） (Card 1288974591)
- 見積件数一覧(見積提案日基準) (Card 765442322)
- 元請け別契約金額(結果確定日基準) (Card 1579225174)
- 契約率(施工店分析） (Card 90992398)
- 完工一覧 (Card 1123284518)
- 月別施工店ごと郵送件数(今期) (Card 868287800)
- 元請け別完工金額 (Card 1715340574)
- 商談未確定率（3ヶ月毎） (Card 1137777881)
- 契約率_グラフ（見積提案日基準） (Card 1010684648)

</details>

#### 🟠 Từ **コラボス_契約率移動平均用** — Feasibility: **LOW** (38% overlap)

- Physical column overlap: **5/13**
- Missing formulas: **3**
- Missing physical cols: **8**

**Missing Formulas** (3):
- `今日まで`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`

#### 🟡 Từ **コラボス＋リペイント（昨対集計用）** — Feasibility: **MEDIUM** (57% overlap)

- Physical column overlap: **4/7**
- Missing formulas: **1**
- Missing physical cols: **3**

**Missing Formulas** (1):
- `集計値の昨対比`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date`
- `昨年集計値`
- `集計値`

### Cards dùng: **コラボス_契約率移動平均用** (2 cards)

<details><summary>Danh sách cards</summary>

- 契約率（12ヶ月移動平均） (Card 532453145)
- 契約率（3ヶ月移動平均） (Card 1866181173)

</details>

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (4% overlap)

- Physical column overlap: **5/118**
- Missing formulas: **130**
- Missing physical cols: **113**

**Missing Formulas** (130):
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
- ... và 100 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 93 nữa

#### 🟠 Từ **コラボス＋リペイント（昨対集計用）** — Feasibility: **LOW** (43% overlap)

- Physical column overlap: **3/7**
- Missing formulas: **2**
- Missing physical cols: **4**

**Missing Formulas** (2):
- `カテゴリ表示順`
- `集計値の昨対比`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date`
- `カテゴリ`
- `昨年集計値`
- `集計値`

### Cards dùng: **コラボス＋リペイント（昨対集計用）** (2 cards)

<details><summary>Danh sách cards</summary>

- 数値進捗（施工店）3ヶ月集計 (Card 206632515)
- 数値進捗（施工店） (Card 118066549)

</details>

#### 🟠 Từ **コラボス_契約率移動平均用** — Feasibility: **LOW** (23% overlap)

- Physical column overlap: **3/13**
- Missing formulas: **4**
- Missing physical cols: **10**

**Missing Formulas** (4):
- `今日まで`
- `元請会社（DCMまとめ）`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (3% overlap)

- Physical column overlap: **4/118**
- Missing formulas: **130**
- Missing physical cols: **114**

**Missing Formulas** (130):
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
- ... và 100 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 94 nữa


---
## 工場売上分析 (Page 248150074)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| ER_売上/受注_直近_PRD | 227 | 330 | 557 |
| ER_現場名入り売上実績 | 267 | 25 | 292 |
| 【大型出荷有無用】ER_売上/受注_直近_PRD | 13 | 6 | 19 |

### Physical Column Overlap Matrix

| Target \ Source | ER_売上/受注_直近_PRD | ER_現場名入り売上実績 | 【大型出荷有無用】ER_売上/受注_直近 |
|:---|:---:|:---:|:---:|
| ER_売上/受注_直近_PRD | - | 🟢 85% (227/267) | 🟢 85% (11/13) |
| ER_現場名入り売上実績 | 🟢 100% (227/227) | - | 🟢 85% (11/13) |
| 【大型出荷有無用】ER_売上/受注_直近 | 🔴 5% (11/227) | 🔴 4% (11/267) | - |

### Cards dùng: **ER_売上/受注_直近_PRD** (11 cards)

<details><summary>Danh sách cards</summary>

- ステータス別_工場・倉庫・施設出荷社数_年比較 (Card 228624032)
- 商品別_工場・倉庫・施設出荷現場数 (Card 674045266)
- ステータス別_工場・倉庫・施設売上 (Card 1924842861)
- 商品別_工場・倉庫・施設出荷社数 (Card 1341591185)
- ステータス別_工場・倉庫・施設出荷現場数 (Card 572002633)
- ステータス別_工場・倉庫・施設出荷_平均単価_年比較 (Card 571321567)
- ステータス別_工場・倉庫・施設売上_年比較 (Card 1712590684)
- ステータス別_工場・倉庫・施設出荷現場数_年比較 (Card 335358071)
- 商品別_工場・倉庫・施設出荷_平均単価 (Card 988661802)
- ステータス別_工場・倉庫・施設出荷_平均単価 (Card 1491562448)
- 材料別_工場・倉庫・施設売上 (Card 647931224)

</details>

#### 🟢 Từ **ER_現場名入り売上実績** — Feasibility: **HIGH** (85% overlap)

- Physical column overlap: **227/267**
- Missing formulas: **10**
- Missing physical cols: **40**

**Missing Formulas** (10):
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

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 20 nữa

#### 🟢 Từ **【大型出荷有無用】ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (85% overlap)

- Physical column overlap: **11/13**
- Missing formulas: **2**
- Missing physical cols: **2**

**Missing Formulas** (2):
- `全社数`
- `出荷済み社数`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `出荷フラグ`
- `建物種別名（工場施設統合）`

### Cards dùng: **【大型出荷有無用】ER_売上/受注_直近_PRD** (2 cards)

<details><summary>Danh sách cards</summary>

- 月別_工場・倉庫・施設出荷社数 (Card 1017947390)
- 出荷済社数_工場・施設 (Card 1734810736)

</details>

#### 🔴 Từ **ER_売上/受注_直近_PRD** — Feasibility: **VERY LOW** (5% overlap)

- Physical column overlap: **11/227**
- Missing formulas: **328**
- Missing physical cols: **214**

**Missing Formulas** (328):
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
- ... và 298 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 196 nữa

#### 🔴 Từ **ER_現場名入り売上実績** — Feasibility: **VERY LOW** (4% overlap)

- Physical column overlap: **11/267**
- Missing formulas: **25**
- Missing physical cols: **254**

**Missing Formulas** (25):
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

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 236 nữa

### Cards dùng: **ER_現場名入り売上実績** (1 cards)

<details><summary>Danh sách cards</summary>

- 工場案件一覧 (Card 1643529095)

</details>

#### 🟢 Từ **ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (100% overlap)

- Physical column overlap: **227/227**
- Missing formulas: **315**
- Missing physical cols: **0**

**Missing Formulas** (315):
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
- ... và 285 nữa

#### 🟢 Từ **【大型出荷有無用】ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (85% overlap)

- Physical column overlap: **11/13**
- Missing formulas: **4**
- Missing physical cols: **2**

**Missing Formulas** (4):
- `全社数`
- `出荷済み社数`
- `加盟店子ランク表示順`
- `売上時期`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `出荷フラグ`
- `建物種別名（工場施設統合）`


---
## 物件種別修正用 (Page 836254252)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| ER_売上/受注_直近_PRD | 227 | 330 | 557 |
| ER_現場名入り売上実績 | 267 | 25 | 292 |
| Store Example Data | 5 | 0 | 5 |
| コラボス＋リペイント | 118 | 131 | 249 |

### Physical Column Overlap Matrix

| Target \ Source | ER_売上/受注_直近_PRD | ER_現場名入り売上実績 | Store Example Data | コラボス＋リペイント |
|:---|:---:|:---:|:---:|:---:|
| ER_売上/受注_直近_PRD | - | 🟢 85% (227/267) | 🔴 0% (0/5) | 🟠 23% (27/118) |
| ER_現場名入り売上実績 | 🟢 100% (227/227) | - | 🔴 0% (0/5) | 🟠 26% (31/118) |
| Store Example Data | 🔴 0% (0/227) | 🔴 0% (0/267) | - | 🔴 0% (0/118) |
| コラボス＋リペイント | 🔴 12% (27/227) | 🔴 12% (31/267) | 🔴 0% (0/5) | - |

### Cards dùng: **ER_現場名入り売上実績** (2 cards)

<details><summary>Danh sách cards</summary>

- ERAWAN_物件種別(すべて) (Card 916494563)
- 物件種別修正用一覧_ERAWAN (Card 1675340749)

</details>

#### 🟢 Từ **ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (100% overlap)

- Physical column overlap: **227/227**
- Missing formulas: **315**
- Missing physical cols: **0**

**Missing Formulas** (315):
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
- ... và 285 nữa

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

#### 🟠 Từ **コラボス＋リペイント** — Feasibility: **LOW** (26% overlap)

- Physical column overlap: **31/118**
- Missing formulas: **123**
- Missing physical cols: **84**

**Missing Formulas** (123):
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
- ... và 93 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- `カテゴリ`
- `キャンペーン`
- `コーナン_加盟金あり`
- `コーナン_加盟金なし`
- ... và 67 nữa

### Cards dùng: **コラボス＋リペイント** (1 cards)

<details><summary>Danh sách cards</summary>

- 物件種別修正用一覧_コラボス (Card 936888329)

</details>

#### 🔴 Từ **ER_売上/受注_直近_PRD** — Feasibility: **VERY LOW** (12% overlap)

- Physical column overlap: **27/227**
- Missing formulas: **320**
- Missing physical cols: **198**

**Missing Formulas** (320):
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
- ... và 290 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 180 nữa

#### 🔴 Từ **ER_現場名入り売上実績** — Feasibility: **VERY LOW** (12% overlap)

- Physical column overlap: **31/267**
- Missing formulas: **16**
- Missing physical cols: **234**

**Missing Formulas** (16):
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

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 216 nữa

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`


---
## 完工予測 (Page 929628649)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| Store Example Data | 5 | 0 | 5 |
| コラボス＋リペイント | 118 | 131 | 249 |
| コラボス＋リペイント（日別集計） | 10 | 11 | 21 |

### Physical Column Overlap Matrix

| Target \ Source | Store Example Data | コラボス＋リペイント | コラボス＋リペイント（日別集計） |
|:---|:---:|:---:|:---:|
| Store Example Data | - | 🔴 0% (0/118) | 🔴 0% (0/10) |
| コラボス＋リペイント | 🔴 0% (0/5) | - | 🟠 40% (4/10) |
| コラボス＋リペイント（日別集計） | 🔴 0% (0/5) | 🔴 3% (4/118) | - |

### Cards dùng: **コラボス＋リペイント（日別集計）** (7 cards)

<details><summary>Danh sách cards</summary>

- 前期 完工粗利進捗（完工・未完工集計） (Card 430670634)
- 坂本あテスト＿  完工粗利進捗（完工・未完工集計） (Card 761208411)
- 月別実績集計表（昨対比較含む） (Card 1175704747)
- 前期 数字進捗集計（案件・見積・契約） (Card 800198233)
- 完工粗利進捗（完工・未完工集計） (Card 476260492)
- 前期 月別実績集計表（昨対比較含む) (Card 1183799360)
- 数字進捗集計（案件・見積・契約） (Card 203300921)

</details>

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (3% overlap)

- Physical column overlap: **4/118**
- Missing formulas: **127**
- Missing physical cols: **114**

**Missing Formulas** (127):
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
- ... và 97 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 94 nữa

### Cards dùng: **コラボス＋リペイント** (9 cards)

<details><summary>Danh sách cards</summary>

- 契約予定物件一覧（※フィルタはかかりません） (Card 917263084)
- 今期 平均工事粗利 (Card 67574147)
- 前期 平均工事粗利 (Card 958787017)
- 工事粗利進捗（完工：確定分、未完工：完了予定日で集計） (Card 1962254929)
- 前期 平均契約金額 (Card 1518625291)
- 完工物件一覧（完工確認済み、支払い基準日入力物件） (Card 255857016)
- 未完工物件一覧（工事完了予定日で抽出） (Card 2071676063)
- 今期 平均契約金額 (Card 1584937308)
- プロテック手数料予実（完工粗利予測） (Card 1918456637)

</details>

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

#### 🟠 Từ **コラボス＋リペイント（日別集計）** — Feasibility: **LOW** (40% overlap)

- Physical column overlap: **4/10**
- Missing formulas: **9**
- Missing physical cols: **4**

**Missing Formulas** (9):
- `カテゴリ_変換`
- `予実不足分`
- `予実不足分（注力）`
- `契約実績`
- `昨対比`
- `期`
- `注力予算`
- `達成率`
- `達成率（注力）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `予算`
- `事業所`
- `営業担当（文字化け修正）`
- `完工/未完工`
- `実績`
- `昨年実績`


---
## プロテック案件実績 (Page 1134665337)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| Store Example Data | 5 | 0 | 5 |
| コラボス＋リペイント | 118 | 131 | 249 |
| コラボス＋リペイント（昨対集計用） | 7 | 2 | 9 |
| 積算チーム遵守率 | 8 | 3 | 11 |

### Physical Column Overlap Matrix

| Target \ Source | Store Example Data | コラボス＋リペイント | コラボス＋リペイント（昨対集計用） | 積算チーム遵守率 |
|:---|:---:|:---:|:---:|:---:|
| Store Example Data | - | 🔴 0% (0/118) | 🔴 0% (0/7) | 🔴 0% (0/8) |
| コラボス＋リペイント | 🔴 0% (0/5) | - | 🟡 57% (4/7) | 🔴 12% (1/8) |
| コラボス＋リペイント（昨対集計用） | 🔴 0% (0/5) | 🔴 3% (4/118) | - | 🔴 0% (0/8) |
| 積算チーム遵守率 | 🔴 0% (0/5) | 🔴 1% (1/118) | 🔴 0% (0/7) | - |

### Cards dùng: **コラボス＋リペイント** (19 cards)

<details><summary>Danh sách cards</summary>

- 島忠_累計新規案件数 (Card 691225406)
- DCM_累計新規案件数 (Card 491639767)
- 週次_DCM新規案件数（コラボス） (Card 400199465)
- 週次_一建設新規案件数（コラボス） (Card 382663062)
- 一建設_累計新規案件数 (Card 1234487589)
- コラボス_累計新規案件数 (Card 1252179431)
- コーナン_累計新規案件数 (Card 1254719814)
- 関西電力_累計新規案件数 (Card 1094235989)
- 週次_ヤマダデンキ新規案件数（コラボス） (Card 431395086)
- ヤマダデンキ_累計新規案件数 (Card 1560170550)
- 週次_コーナン新規案件数（コラボス） (Card 620429819)
- 週次_新規案件数（コラボス） (Card 2133931667)
- 週次_アイリスプラザ新規案件数（コラボス） (Card 2060477552)
- コラボス_元請け別新規案件数 (Card 1517610841)
- 月次_新規案件数（コラボス） (Card 222570016)
- アイリスプラザ_累計新規案件数 (Card 25999181)
- 案件一覧 (Card 1039323943)
- 週次_島忠新規案件数（コラボス） (Card 1322336018)
- 週次_関西電力新規案件数（コラボス） (Card 1483605998)

</details>

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

#### 🟡 Từ **コラボス＋リペイント（昨対集計用）** — Feasibility: **MEDIUM** (57% overlap)

- Physical column overlap: **4/7**
- Missing formulas: **1**
- Missing physical cols: **3**

**Missing Formulas** (1):
- `集計値の昨対比`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date`
- `昨年集計値`
- `集計値`

#### 🔴 Từ **積算チーム遵守率** — Feasibility: **VERY LOW** (12% overlap)

- Physical column overlap: **1/8**
- Missing formulas: **3**
- Missing physical cols: **6**

**Missing Formulas** (3):
- `対応件数`
- `対象件数`
- `遵守率`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `元請名`
- `判定`
- `営業日数`
- `翌営業日`
- `見積提出日`
- `訪問月`
- `顧客名`

### Cards dùng: **コラボス＋リペイント（昨対集計用）** (1 cards)

<details><summary>Danh sách cards</summary>

- コラボス_元請会社別新規案件数（昨対比）. (Card 131473852)

</details>

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (3% overlap)

- Physical column overlap: **4/118**
- Missing formulas: **130**
- Missing physical cols: **114**

**Missing Formulas** (130):
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
- ... và 100 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 94 nữa

#### 🔴 Từ **積算チーム遵守率** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/8**
- Missing formulas: **3**
- Missing physical cols: **8**

**Missing Formulas** (3):
- `対応件数`
- `対象件数`
- `遵守率`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `元請名`
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

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| ER_売上/受注_直近_PRD | 227 | 330 | 557 |
| 【大型出荷有無用】ER_売上/受注_直近_PRD | 13 | 6 | 19 |

### Physical Column Overlap Matrix

| Target \ Source | ER_売上/受注_直近_PRD | 【大型出荷有無用】ER_売上/受注_直近 |
|:---|:---:|:---:|
| ER_売上/受注_直近_PRD | - | 🟢 85% (11/13) |
| 【大型出荷有無用】ER_売上/受注_直近 | 🔴 5% (11/227) | - |

### Cards dùng: **ER_売上/受注_直近_PRD** (11 cards)

<details><summary>Danh sách cards</summary>

- 商品別_アパマン出荷現場数 (Card 1228599687)
- ステータス別_アパマン出荷現場数 (Card 1098878064)
- ステータス別_アパマン出荷現場数_年比較 (Card 1653484524)
- ステータス別_アパマン出荷_平均単価 (Card 36646733)
- ステータス別_アパマン売上 (Card 1538070797)
- ステータス別_アパマン売上_年比較 (Card 23606368)
- 材料別_アパマン売上 (Card 1200401997)
- ステータス別_アパマン出荷社数_年比較 (Card 1515399157)
- ステータス別_ アパマン 出荷_平均単価_年比較 (Card 975517784)
- 商品別_アパマン出荷社数 (Card 551221377)
- 商品別_アパマン出荷_平均単価 (Card 753260540)

</details>

#### 🟢 Từ **【大型出荷有無用】ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (85% overlap)

- Physical column overlap: **11/13**
- Missing formulas: **2**
- Missing physical cols: **2**

**Missing Formulas** (2):
- `全社数`
- `出荷済み社数`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `出荷フラグ`
- `建物種別名（工場施設統合）`

### Cards dùng: **【大型出荷有無用】ER_売上/受注_直近_PRD** (2 cards)

<details><summary>Danh sách cards</summary>

- 月別_アパマン出荷社数 (Card 1037821389)
- 出荷済社数_アパマン (Card 222412946)

</details>

#### 🔴 Từ **ER_売上/受注_直近_PRD** — Feasibility: **VERY LOW** (5% overlap)

- Physical column overlap: **11/227**
- Missing formulas: **328**
- Missing physical cols: **214**

**Missing Formulas** (328):
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
- ... và 298 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 196 nữa


---
## 商談未確定・郵送件数検索 (Page 1281028522)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| Store Example Data | 5 | 0 | 5 |
| コラボス＋リペイント | 118 | 131 | 249 |

### Physical Column Overlap Matrix

| Target \ Source | Store Example Data | コラボス＋リペイント |
|:---|:---:|:---:|
| Store Example Data | - | 🔴 0% (0/118) |
| コラボス＋リペイント | 🔴 0% (0/5) | - |

### Cards dùng: **コラボス＋リペイント** (18 cards)

<details><summary>Danh sách cards</summary>

- 月別元請けごと郵送件数(前期) (Card 501835661)
- その他元請別商談未確定件数(見積提案日基準) (Card 745437269)
- 郵送未確定率(今月) (Card 793217449)
- 月別元請けごと商談未確定件数(今期) (Card 1458968856)
- 商談未確定率(見積提案日基準) (Card 1851052092)
- 郵送案件一覧(見積提案日基準) (Card 849120903)
- 月別施工店ごと郵送件数(今期) (Card 868287800)
- 注力元請別商談未確定件数(見積提案日基準) (Card 375432919)
- 月別施工店ごと郵送件数(前期) (Card 1274644734)
- 郵送合計件数(見積提案日基準) (Card 1392125953)
- 注力元請別郵送件数(今月) (Card 1148770875)
- 月別元請けごと商談未確定案件数(前期) (Card 1409183744)
- 月別元請けごと郵送件数(今期) (Card 999361246)
- 商談日未確定案件一覧(見積提案日基準) (Card 719910242)
- 月別施工店ごと商談未確定件数(前期) (Card 2144385797)
- その他元請別郵送件数(今月) (Card 1669657755)
- 商談未確定案件数(見積提案日基準) (Card 390114331)
- 月別施工店ごと商談未確定件数(今期) (Card 138189276)

</details>

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`


---
## コラボス集計 (Page 1428843185)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| コラボス_契約率移動平均用 | 13 | 4 | 17 |
| コラボス集計 | 92 | 13 | 105 |
| コラボス＋リペイント | 118 | 131 | 249 |

### Physical Column Overlap Matrix

| Target \ Source | コラボス_契約率移動平均用 | コラボス集計 | コラボス＋リペイント |
|:---|:---:|:---:|:---:|
| コラボス_契約率移動平均用 | - | 🔴 5% (5/92) | 🔴 4% (5/118) |
| コラボス集計 | 🟠 38% (5/13) | - | 🟡 69% (82/118) |
| コラボス＋リペイント | 🟠 38% (5/13) | 🟢 89% (82/92) | - |

### Cards dùng: **コラボス＋リペイント** (32 cards)

<details><summary>Danh sách cards</summary>

- 見積提出数_グラフ（見積提案日基準） (Card 1887804995)
- 見積提出数_60万以上_グラフ（見積提案日基準） (Card 164598919)
- 契約金額_グラフ（結果確定日基準） (Card 17212857)
- 契約金額 (Card 1492756894)
- 完工数_グラフ（工事完了日基準） (Card 779700125)
- 契約数_60万以上 (Card 1889903978)
- 完工数_60万以上 (Card 691201626)
- 見積提案数 (Card 1532260531)
- 完工金額_60万以上_グラフ（工事完了日基準） (Card 1966591176)
- 案件数_60万以上 (Card 1718162296)
- 契約金額_60万以上 (Card 2075585989)
- 完工数_60万以上_グラフ（工事完了日基準） (Card 1754595176)
- 案件数 (Card 41490049)
- 契約数_グラフ（結果確定日基準） (Card 531776962)
- 工事粗利_60万以上 (Card 1048755699)
- 見積提案数_60万以上 (Card 1520589725)
- 完工金額 (Card 1768862313)
- 工事粗利_グラフ（支払基準日基準） (Card 1868388949)
- 工事粗利_60万以上_グラフ（支払基準日基準） (Card 821020907)
- 契約率（見積提案日基準・60万以上） (Card 82040535)
- 案件数_60万以上_グラフ (Card 1653813382)
- 完工金額_グラフ（工事完了日基準） (Card 1546556308)
- 完工金額_60万以上 (Card 1573144144)
- 工事粗利 (Card 894907839)
- 案件発生数_グラフ（承り日基準） (Card 1952258545)
- 契約率（見積提案日基準） (Card 1192997370)
- 契約率_グラフ（見積提案日基準・60万以上） (Card 308637114)
- 契約金額__60万以上 グラフ（結果確定日基準） (Card 379469956)
- 契約数 (Card 1596693498)
- 契約率_グラフ（見積提案日基準） (Card 1010684648)
- 完工数 (Card 1813675019)
- 契約数_60万以上_グラフ（結果確定日基準） (Card 1846390561)

</details>

#### 🟠 Từ **コラボス_契約率移動平均用** — Feasibility: **LOW** (38% overlap)

- Physical column overlap: **5/13**
- Missing formulas: **3**
- Missing physical cols: **8**

**Missing Formulas** (3):
- `今日まで`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`

#### 🟢 Từ **コラボス集計** — Feasibility: **HIGH** (89% overlap)

- Physical column overlap: **82/92**
- Missing formulas: **6**
- Missing physical cols: **9**

**Missing Formulas** (6):
- `プロテック請負金額（合計）`
- `契約率（3ヶ月移動平均・60万円以上）`
- `契約率（3ヶ月移動平均）`
- `平均契約金額`
- `検討中案件数`
- `見積①提出数`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `ステータス`
- `契約件数（3ヶ月移動平均・60万以上）`
- `契約件数（3ヶ月移動平均）`
- `実績判断`
- `工事粗利`
- `手数料確度`
- `期待値の計上日`
- `確度用ステージ`
- `見積提案件数（3ヶ月移動平均・60万以上）`
- `見積提案件数（3ヶ月移動平均）`

### Cards dùng: **コラボス_契約率移動平均用** (4 cards)

<details><summary>Danh sách cards</summary>

- 契約率（3ヶ月移動平均/60万円以上） (Card 988197674)
- 契約率（12ヶ月移動平均） (Card 532453145)
- 契約率（3ヶ月移動平均） (Card 1866181173)
- 契約率（12ヶ月移動平均/60万円以上） (Card 909334434)

</details>

#### 🔴 Từ **コラボス集計** — Feasibility: **VERY LOW** (5% overlap)

- Physical column overlap: **5/92**
- Missing formulas: **12**
- Missing physical cols: **87**

**Missing Formulas** (12):
- `プロテック請負金額（合計）`
- `契約件数`
- `契約件数達成率`
- `契約率`
- `契約率（3ヶ月移動平均・60万円以上）`
- `契約金額達成率`
- `完工粗利予算（注力）`
- `平均契約金額`
- `検討中案件数`
- `見積①提出数`
- `見積提案年`
- `見積提案月`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 67 nữa

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (4% overlap)

- Physical column overlap: **5/118**
- Missing formulas: **130**
- Missing physical cols: **113**

**Missing Formulas** (130):
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
- ... và 100 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 93 nữa


---
## 全体管理 (Page 1827358914)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| ER_受注/出荷_直近_PRD | 222 | 100 | 321 |
| ER_売上/受注_直近_PRD | 227 | 330 | 557 |
| コラボス_契約率移動平均用 | 13 | 4 | 17 |
| コラボス＋リペイント | 118 | 131 | 249 |

### Physical Column Overlap Matrix

| Target \ Source | ER_受注/出荷_直近_PRD | ER_売上/受注_直近_PRD | コラボス_契約率移動平均用 | コラボス＋リペイント |
|:---|:---:|:---:|:---:|:---:|
| ER_受注/出荷_直近_PRD | - | 🟢 82% (186/227) | 🔴 0% (0/13) | 🔴 19% (23/118) |
| ER_売上/受注_直近_PRD | 🟢 84% (186/222) | - | 🔴 0% (0/13) | 🟠 23% (27/118) |
| コラボス_契約率移動平均用 | 🔴 0% (0/222) | 🔴 0% (0/227) | - | 🔴 4% (5/118) |
| コラボス＋リペイント | 🔴 10% (23/222) | 🔴 12% (27/227) | 🟠 38% (5/13) | - |

### Cards dùng: **コラボス＋リペイント** (43 cards)

<details><summary>Danh sách cards</summary>

- 他社塗料購入粗利 (Card 1302356523)
- 完工件数 (Card 1802584313)
- 紹介モデル手数料 (Card 417208681)
- 契約件数 (Card 1881220917)
- 工場塗料粗利_グラフ (Card 583145161)
- アパマン_塗料粗利 (Card 643073117)
- 契約件数_グラフ (Card 1551637113)
- カイゼンReペイント＆工場アパマン手数料 予実 (Card 747665703)
- 契約率（見積提案日基準・60万以上） (Card 82040535)
- 法人営業部_塗料粗利予実表_当月 (Card 991329451)
- 沖縄_塗料注文件数_グラフ (Card 1307059860)
- 法人営業部_塗料粗利 予実 (Card 742909363)
- 大規模修繕 (Card 381801388)
- 工事粗利_グラフ (Card 703377110)
- プロテック塗料粗利 (Card 1519241531)
- 工場・アパマン塗料粗利_グラフ (Card 1540274693)
- 工場アパマン成約手数料_グラフ (Card 264124591)
- プロテック塗料注文件数 (Card 1757213491)
- 大規模修繕注文件数_グラフ (Card 2090189264)
- 工場アパマン紹介手数料 (Card 612296022)
- プロテック手数料 予実 (Card 1108873039)
- 法人営業部_手数料予実_当月 (Card 1607768844)
- 法人営業部_塗料粗利 予実 (Card 798110155)
- 工場・アパマン_塗料粗利 (Card 119774191)
- 法人営業部_塗料粗利 予実 (Card 1140052288)
- 沖縄_塗料粗利 (Card 908199668)
- 工事粗利 (Card 1417532884)
- プロテック塗料粗利 (Card 1562411866)
- 工場・アパマン塗料注文件数_グラフ (Card 198091187)
- 工場アパマン紹介手数料_グラフ (Card 223021489)
- アパマン塗料注文件数_グラフ (Card 199640344)
- CAD作成代行費用（プロテック） (Card 1897760483)
- 工場塗料注文件数_グラフ (Card 282162621)
- 工場_塗料粗利 (Card 870418362)
- 完工件数_グラフ (Card 144862465)
- 契約率（見積提案日基準） (Card 1192997370)
- 法人営業部_全体予実 (Card 1635302702)
- 大規模修繕粗利_グラフ (Card 1013435713)
- 施工店登録費用 (Card 671546784)
- 法人営業部_塗料粗利 予実（経理確認用） (Card 325383362)
- 工場アパマン成約手数料 (Card 1480269791)
- 沖縄_塗料粗利_グラフ (Card 814591635)
- アパマン塗料粗利_グラフ (Card 1455082981)

</details>

#### 🔴 Từ **ER_受注/出荷_直近_PRD** — Feasibility: **VERY LOW** (10% overlap)

- Physical column overlap: **23/222**
- Missing formulas: **90**
- Missing physical cols: **199**

**Missing Formulas** (90):
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
- ... và 60 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 179 nữa

#### 🔴 Từ **ER_売上/受注_直近_PRD** — Feasibility: **VERY LOW** (12% overlap)

- Physical column overlap: **27/227**
- Missing formulas: **320**
- Missing physical cols: **198**

**Missing Formulas** (320):
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
- ... và 290 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 180 nữa

#### 🟠 Từ **コラボス_契約率移動平均用** — Feasibility: **LOW** (38% overlap)

- Physical column overlap: **5/13**
- Missing formulas: **3**
- Missing physical cols: **8**

**Missing Formulas** (3):
- `今日まで`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `60万円以上`
- `契約率集計用年`
- `契約率集計用月`
- `平均期間`
- `日付軸`
- `月別契約件数`
- `月別見積件数`
- `結果/見積`

### Cards dùng: **ER_売上/受注_直近_PRD** (1 cards)

<details><summary>Danh sách cards</summary>

- 商品別売上（カイゼンReペイント）_グラフ (Card 308568308)

</details>

#### 🟢 Từ **ER_受注/出荷_直近_PRD** — Feasibility: **HIGH** (84% overlap)

- Physical column overlap: **186/222**
- Missing formulas: **55**
- Missing physical cols: **36**

**Missing Formulas** (55):
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
- ... và 25 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 16 nữa

#### 🔴 Từ **コラボス_契約率移動平均用** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/13**
- Missing formulas: **4**
- Missing physical cols: **13**

**Missing Formulas** (4):
- `今日まで`
- `元請会社（DCMまとめ）`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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

#### 🟠 Từ **コラボス＋リペイント** — Feasibility: **LOW** (23% overlap)

- Physical column overlap: **27/118**
- Missing formulas: **121**
- Missing physical cols: **89**

**Missing Formulas** (121):
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
- ... và 91 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 71 nữa

### Cards dùng: **コラボス_契約率移動平均用** (2 cards)

<details><summary>Danh sách cards</summary>

- 契約率（3ヶ月移動平均） (Card 1866181173)
- 契約率（3ヶ月移動平均/60万円以上） (Card 988197674)

</details>

#### 🔴 Từ **ER_受注/出荷_直近_PRD** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/222**
- Missing formulas: **100**
- Missing physical cols: **222**

**Missing Formulas** (100):
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
- ... và 70 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 202 nữa

#### 🔴 Từ **ER_売上/受注_直近_PRD** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/227**
- Missing formulas: **330**
- Missing physical cols: **227**

**Missing Formulas** (330):
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
- ... và 300 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 207 nữa

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (4% overlap)

- Physical column overlap: **5/118**
- Missing formulas: **130**
- Missing physical cols: **113**

**Missing Formulas** (130):
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
- ... và 100 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 93 nữa

### Cards dùng: **ER_受注/出荷_直近_PRD** (1 cards)

<details><summary>Danh sách cards</summary>

- 商品別売上（カイゼンReペイント） (Card 1092187899)

</details>

#### 🟢 Từ **ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (82% overlap)

- Physical column overlap: **186/227**
- Missing formulas: **286**
- Missing physical cols: **41**

**Missing Formulas** (286):
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
- ... và 256 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 21 nữa

#### 🔴 Từ **コラボス_契約率移動平均用** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/13**
- Missing formulas: **4**
- Missing physical cols: **13**

**Missing Formulas** (4):
- `今日まで`
- `元請会社（DCMまとめ）`
- `契約率集計用日付`
- `契約率（3ヶ月移動平均）`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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

#### 🔴 Từ **コラボス＋リペイント** — Feasibility: **VERY LOW** (19% overlap)

- Physical column overlap: **23/118**
- Missing formulas: **123**
- Missing physical cols: **93**

**Missing Formulas** (123):
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
- ... và 93 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 75 nữa


---
## 週間MTG用コラボス分析 (Page 1959758463)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| コラボス集計 | 92 | 13 | 105 |
| コラボス＋リペイント | 118 | 131 | 249 |

### Physical Column Overlap Matrix

| Target \ Source | コラボス集計 | コラボス＋リペイント |
|:---|:---:|:---:|
| コラボス集計 | - | 🟡 69% (82/118) |
| コラボス＋リペイント | 🟢 89% (82/92) | - |

### Cards dùng: **コラボス集計** (1 cards)

<details><summary>Danh sách cards</summary>

- 【期待値込】プロテック請負金額集計_元請別（計上予定日基準） (Card 1255037399)

</details>

#### 🟡 Từ **コラボス＋リペイント** — Feasibility: **MEDIUM** (69% overlap)

- Physical column overlap: **82/118**
- Missing formulas: **123**
- Missing physical cols: **36**

**Missing Formulas** (123):
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
- ... và 93 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 16 nữa

### Cards dùng: **コラボス＋リペイント** (15 cards)

<details><summary>Danh sách cards</summary>

- 見積予実_元請別 (Card 587114568)
- 平均見積金額_元請別(直近1年間) (Card 44262708)
- 平均日数_施工店別 (Card 1861520957)
- 契約予実_元請別 (Card 460265818)
- 完工予実_元請別 (Card 570077680)
- 施工店請負金額_施工店別（工事完了日基準） (Card 1376120614)
- 現調数_施工店別（訪問日基準） (Card 370751928)
- 契約予実_担当別 (Card 1787571010)
- 対応案件数_施工店別（見積提案日基準） (Card 821964464)
- 契約数_施工店別（結果確定日基準） (Card 25377069)
- 見積予実_担当別 (Card 1037568660)
- 完工予実_元請別（注力外） (Card 496855862)
- 完工予実_担当別 (Card 526521217)
- 平均見積金額_元請別(直近3ヶ月) (Card 1704425485)
- プロテック請負金額集計_担当別 (Card 1171272019)

</details>

#### 🟢 Từ **コラボス集計** — Feasibility: **HIGH** (89% overlap)

- Physical column overlap: **82/92**
- Missing formulas: **6**
- Missing physical cols: **9**

**Missing Formulas** (6):
- `プロテック請負金額（合計）`
- `契約率（3ヶ月移動平均・60万円以上）`
- `契約率（3ヶ月移動平均）`
- `平均契約金額`
- `検討中案件数`
- `見積①提出数`

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `ステータス`
- `契約件数（3ヶ月移動平均・60万以上）`
- `契約件数（3ヶ月移動平均）`
- `実績判断`
- `工事粗利`
- `手数料確度`
- `期待値の計上日`
- `確度用ステージ`
- `見積提案件数（3ヶ月移動平均・60万以上）`
- `見積提案件数（3ヶ月移動平均）`


---
## 法人営業部用_売上集計(出荷日基準) (Page 2006619322)

### Datasets

| Dataset | Physical | Formula | Total |
|:---|:---:|:---:|:---:|
| ER_受注/出荷_直近_PRD | 222 | 100 | 321 |
| ER_売上/受注_直近_PRD | 227 | 330 | 557 |
| ER_現場名入り受注 | 257 | 31 | 288 |
| Store Example Data | 5 | 0 | 5 |

### Physical Column Overlap Matrix

| Target \ Source | ER_受注/出荷_直近_PRD | ER_売上/受注_直近_PRD | ER_現場名入り受注 | Store Example Data |
|:---|:---:|:---:|:---:|:---:|
| ER_受注/出荷_直近_PRD | - | 🟢 82% (186/227) | 🟢 86% (222/257) | 🔴 0% (0/5) |
| ER_売上/受注_直近_PRD | 🟢 84% (186/222) | - | 🟡 72% (186/257) | 🔴 0% (0/5) |
| ER_現場名入り受注 | 🟢 100% (222/222) | 🟢 82% (186/227) | - | 🔴 0% (0/5) |
| Store Example Data | 🔴 0% (0/222) | 🔴 0% (0/227) | 🔴 0% (0/257) | - |

### Cards dùng: **ER_受注/出荷_直近_PRD** (3 cards)

<details><summary>Danh sách cards</summary>

- Duplicate of 次の複製： 売上集計表(出荷日基準) (Card 260858484)
- Duplicate of 次の複製： 売上実績(出荷日基準) (Card 1258504332)
- Duplicate of 売上集計表 (Card 948537816)

</details>

#### 🟢 Từ **ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (82% overlap)

- Physical column overlap: **186/227**
- Missing formulas: **286**
- Missing physical cols: **41**

**Missing Formulas** (286):
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
- ... và 256 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 21 nữa

#### 🟢 Từ **ER_現場名入り受注** — Feasibility: **HIGH** (86% overlap)

- Physical column overlap: **222/257**
- Missing formulas: **15**
- Missing physical cols: **35**

**Missing Formulas** (15):
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

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 15 nữa

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

### Cards dùng: **ER_現場名入り受注** (1 cards)

<details><summary>Danh sách cards</summary>

- Duplicate of 次の複製： 売上詳細(出荷日基準) (Card 289460039)

</details>

#### 🟢 Từ **ER_受注/出荷_直近_PRD** — Feasibility: **HIGH** (100% overlap)

- Physical column overlap: **222/222**
- Missing formulas: **83**
- Missing physical cols: **0**

**Missing Formulas** (83):
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
- ... và 53 nữa

#### 🟢 Từ **ER_売上/受注_直近_PRD** — Feasibility: **HIGH** (82% overlap)

- Physical column overlap: **186/227**
- Missing formulas: **317**
- Missing physical cols: **41**

**Missing Formulas** (317):
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
- ... và 287 nữa

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
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
- ... và 21 nữa

#### 🔴 Từ **Store Example Data** — Feasibility: **VERY LOW** (0% overlap)

- Physical column overlap: **0/5**
- Missing formulas: **0**
- Missing physical cols: **5**

**Physical columns KHÔNG có trong dataset đích** (cản trở tạo formula):
- `date_ymd`
- `department`
- `revenue`
- `sales_rep`
- `state`

