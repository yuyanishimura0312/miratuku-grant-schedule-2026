# 助成金申請 必要書類セット — ミラツク／esse-sense 2026

340件の助成金ドラフトに対する必要書類を体系化したマスターパッケージ。

## 構成

```
required_docs/
├── README.md                       (このファイル)
├── _ミラツク_共通書類/
│   └── INDEX.md                    (NPO法人ミラツクの法人書類所在ガイド)
├── _esse-sense_共通書類/
│   └── INDEX.md                    (株式会社エッセンスの法人書類所在ガイド)
├── _共通テンプレート/
│   ├── M_法人概要.md               (ミラツク法人概要・申請書セクション1原稿)
│   ├── E_法人概要.md               (esse-sense法人概要・申請書セクション1原稿)
│   ├── 数値ファクトブック.md       (数値の確定情報集)
│   └── M_E_強み一覧.md             (7つの強み×助成金マッピング)
└── _チェックリスト/
    ├── master_checklist.md         (統合マスターチェックリスト)
    └── grant_specific/             (338件の個別チェックリスト)
        ├── 001_E_観光庁オーバーツーリズム対策.md
        ├── 001_M_観光庁オーバーツーリズム対策.md
        └── ... (338件)
```

## 使い方

### Step 1: 提出予定の助成金を特定
- `drafts_v2/{ID}_{M|E}_{助成金名}.md` で本文ドラフトを確認
- 締切と提出方式を `08_統合実行計画.md` で確認

### Step 2: 必要書類を集める
1. **共通書類** から開始
   - ミラツク（NPO）: `_ミラツク_共通書類/INDEX.md` の各ファイルを取得
   - esse-sense（株式会社）: `_esse-sense_共通書類/INDEX.md` の各ファイルを取得
   - 印鑑証明書・納税証明書は提出直前に取得（有効期限3ヶ月）

2. **マスターチェックリスト**を確認
   - `_チェックリスト/master_checklist.md` で抜け漏れを防止

3. **助成金固有のチェックリスト**を確認
   - `_チェックリスト/grant_specific/{該当ファイル}.md` で固有要件を確認

4. **法人概要・強み資料**を準備
   - 申請書本文の数値データを `_共通テンプレート/数値ファクトブック.md` から引用
   - 訴求テーマを `_共通テンプレート/M_E_強み一覧.md` から選択

### Step 3: 申請書本体を作成
- `drafts_v2/` のドラフトを起点に、公募要領の指定様式へ転記
- HTML版: `drafts_html/` または公開URL https://yuyanishimura0312.github.io/miratuku-grant-schedule-2026/

### Step 4: 提出前チェック
- `_チェックリスト/master_checklist.md` の F. 提出前最終チェック を実施
- 不備対応の連絡先を控えて提出

## ソース書類の所在（要点）

### NPO法人ミラツク 第14期/15期
- 決算書（活動計算書/貸借対照表/財産目録）: `~/Documents/ミラツク事業/ミラツク/NPO法人運営/事業計画・報告/事業報告/2024年/`, `2025年/`
- 事業報告書: 同上フォルダ
- 役員名簿/社員名簿: 同上フォルダ

### 株式会社エッセンス 第04期
- 決算報告書: `~/Documents/ミラツク事業/esse-sense/法人運営/第04期決算報告書.pdf`
- 定款（最新版）: `~/Documents/ミラツク事業/esse-sense/法人運営/法人手続き関連/定款20210901.pdf`
- 法人登記簿: `~/Documents/ミラツク事業/esse-sense/事業計画/esse-sense資料/株式会社エッセンス法人登記簿（全部事項）2023031000171897.PDF`
- 株主名簿: `~/Documents/ミラツク事業/esse-sense/法人運営/【エッセンス】株主名簿.pdf`

### 都度取得が必要な書類
- 印鑑証明書（法務局・3ヶ月以内）
- 履歴事項全部証明書（法務局・3ヶ月以内）
- 納税証明書（税務署・3ヶ月以内）



## ソース書類クイックリンク（クリックでFinder/Preview起動・macOS専用）

### NPO法人ミラツク
| 書類 | リンク |
|------|------|
| 第15期決算書 活動計算書 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/NPO%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB%E3%83%BB%E5%A0%B1%E5%91%8A/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A/2025%E5%B9%B4/%E7%AC%AC15%E6%9C%9F%E6%B1%BA%E7%AE%97%E6%9B%B8_1%E6%B4%BB%E5%8B%95%E8%A8%88%E7%AE%97%E6%9B%B8.pdf) |
| 第15期決算書 貸借対照表 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/NPO%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB%E3%83%BB%E5%A0%B1%E5%91%8A/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A/2025%E5%B9%B4/%E7%AC%AC15%E6%9C%9F%E6%B1%BA%E7%AE%97%E6%9B%B8_2%E8%B2%B8%E5%80%9F%E5%AF%BE%E7%85%A7%E8%A1%A8.pdf) |
| 第14期決算書 活動計算書 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/NPO%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB%E3%83%BB%E5%A0%B1%E5%91%8A/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A/2024%E5%B9%B4/%E7%AC%AC14%E6%9C%9F%E6%B1%BA%E7%AE%97%E6%9B%B8_1%E6%B4%BB%E5%8B%95%E8%A8%88%E7%AE%97%E6%9B%B8.pdf) |
| 役員名簿2024 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/NPO%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB%E3%83%BB%E5%A0%B1%E5%91%8A/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A/2024%E5%B9%B4/%E5%BD%B9%E5%93%A1%E5%90%8D%E7%B0%BF2024.pdf) |
| 社員名簿2025 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/NPO%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB%E3%83%BB%E5%A0%B1%E5%91%8A/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A/2025%E5%B9%B4/%E7%A4%BE%E5%93%A1%E5%90%8D%E7%B0%BF2025.pdf) |
| 事業報告書2025 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/NPO%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB%E3%83%BB%E5%A0%B1%E5%91%8A/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A/2025%E5%B9%B4/%E4%BA%8B%E6%A5%AD%E5%A0%B1%E5%91%8A%E6%9B%B82025.pdf) |
| 履歴事項全部証明書（沖縄公庫提出版） | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/esse-sense/%E8%9E%8D%E8%B3%87%E3%83%BB%E7%94%B3%E8%AB%8B/%E8%9E%8D%E8%B3%87%E9%96%A2%E9%80%A3/%E6%B2%96%E7%B8%84%E5%85%AC%E5%BA%AB/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E7%99%BB%E8%A8%98%E4%BA%8B%E9%A0%85.pdf) |

### 株式会社エッセンス
| 書類 | リンク |
|------|------|
| 第04期決算報告書 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/esse-sense/%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E7%AC%AC04%E6%9C%9F%E6%B1%BA%E7%AE%97%E5%A0%B1%E5%91%8A%E6%9B%B8.pdf) |
| 定款（2021/9/1最新版） | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/esse-sense/%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E6%B3%95%E4%BA%BA%E6%89%8B%E7%B6%9A%E3%81%8D%E9%96%A2%E9%80%A3/%E5%AE%9A%E6%AC%BE20210901.pdf) |
| 株式会社エッセンス法人登記簿 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/esse-sense/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB/esse-sense%E8%B3%87%E6%96%99/%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE%E3%82%A8%E3%83%83%E3%82%BB%E3%83%B3%E3%82%B9%E6%B3%95%E4%BA%BA%E7%99%BB%E8%A8%98%E7%B0%BF%EF%BC%88%E5%85%A8%E9%83%A8%E4%BA%8B%E9%A0%85%EF%BC%892023031000171897.PDF) |
| 株主名簿 | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/esse-sense/%E6%B3%95%E4%BA%BA%E9%81%8B%E5%96%B6/%E3%80%90%E3%82%A8%E3%83%83%E3%82%BB%E3%83%B3%E3%82%B9%E3%80%91%E6%A0%AA%E4%B8%BB%E5%90%8D%E7%B0%BF.pdf) |
| 役員経歴（説明資料2023） | [開く](file:///Users/nishimura%2B/Documents/%E3%83%9F%E3%83%A9%E3%83%84%E3%82%AF%E4%BA%8B%E6%A5%AD/esse-sense/%E4%BA%8B%E6%A5%AD%E8%A8%88%E7%94%BB/esse-sense%E8%B3%87%E6%96%99/%E3%82%A8%E3%83%83%E3%82%BB%E3%83%B3%E3%82%B9%E8%AA%AC%E6%98%8E%E8%B3%87%E6%96%992023_%E5%BD%B9%E5%93%A1%E7%B5%8C%E6%AD%B4.pdf) |

詳細は各 INDEX.md 参照:
- [ミラツク INDEX](_ミラツク_共通書類/INDEX.md)
- [esse-sense INDEX](_esse-sense_共通書類/INDEX.md)

## 統計
- 助成金ドラフト総数: 338件（M=ミラツク+E=esse-sense）
- 個別チェックリスト: 338件
- 共通書類カテゴリ: 6カテゴリ（A法人/B事業実績/C申請書本体/D主体別/E助成金カテゴリ/F提出前）
- マスターチェック項目: 60項目超

## 更新履歴
- 2026-05-10: 初版作成（340件の助成金ドラフト + 必要書類体系化）
