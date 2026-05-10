# 汚染ドラフト報告書

Wave 2/3でcodex並列処理時に発生した汚染drafts（codex実行ログ混入）の一覧。

## 概要
- 全drafts: 338件
- 健全drafts: 165件
- 汚染drafts: 173件

## 症状
冒頭にヘッダのみが配置され、各セクション本文が欠如。代わりにcodexの探索ログ（`exec /bin/bash...`, `succeeded in`, `ls -la`の出力等）が末尾に混入。

## 影響
- 当該drafts_html/*.htmlは表示可能だが内容空（再生成必要）
- required_docs/_チェックリスト/grant_specific/*.md は#6セクションが空となる

## 対処方針
1. **短期**: 汚染ファイルに警告ヘッダ追加、HTML再生成、公開siteへ反映
2. **中期**: codexで再生成（プロンプト見直し、サンドボックスをworkspace-readに変更）
3. **長期**: リカバリ完了後にこのレポートを削除

## 影響を受けるファイル
詳細は contaminated_drafts.txt 参照（173件）
