#!/usr/bin/env python3
"""38 MDドラフトをHTMLに変換し、index.htmlを生成"""
import os, re, glob, html

DRAFTS_MD = "/Users/nishimura+/work/miratuku-grants-2026/drafts_v2"
DRAFTS_HTML = "/Users/nishimura+/work/miratuku-grants-2026/drafts_html"
TEMPLATE = open(f"{DRAFTS_HTML}/_template.html").read()

def md_to_html(md):
    """簡易Markdown → HTML変換"""
    lines = md.split('\n')
    out = []
    in_list = False
    list_type = None
    in_para = False
    para_buf = []

    def flush_para():
        nonlocal in_para, para_buf
        if para_buf:
            text = ' '.join(para_buf).strip()
            if text:
                out.append(f'<p>{text}</p>')
            para_buf.clear()
        in_para = False

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            out.append(f'</{list_type}>')
            in_list = False
            list_type = None

    def inline(s):
        # bold
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        # italic（**で囲まれてないもののみ）
        s = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', s)
        # link
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
        # bare URL
        s = re.sub(r'(?<![">\(])(https?://[^\s<]+)', r'<a href="\1">\1</a>', s)
        # code
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        # checkbox - [ ] / - [x]
        s = re.sub(r'\[\s\]', '<input type="checkbox" disabled>', s)
        s = re.sub(r'\[x\]', '<input type="checkbox" disabled checked>', s, flags=re.IGNORECASE)
        return s

    for raw in lines:
        line = raw.rstrip()
        if not line:
            flush_para()
            flush_list()
            continue
        # ヘッダ
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            flush_para(); flush_list()
            level = len(m.group(1))
            out.append(f'<h{level}>{inline(m.group(2))}</h{level}>')
            continue
        # 区切り線
        if re.match(r'^---+$', line) or re.match(r'^\*\*\*+$', line):
            flush_para(); flush_list()
            out.append('<hr>')
            continue
        # 引用
        if line.startswith('> '):
            flush_para(); flush_list()
            out.append(f'<blockquote>{inline(line[2:])}</blockquote>')
            continue
        # 順序なしリスト
        m = re.match(r'^[\-\*]\s+(.+)$', line)
        if m:
            flush_para()
            if not in_list or list_type != 'ul':
                flush_list()
                out.append('<ul>')
                in_list = True
                list_type = 'ul'
            out.append(f'<li>{inline(m.group(1))}</li>')
            continue
        # 順序付きリスト
        m = re.match(r'^\d+\.\s+(.+)$', line)
        if m:
            flush_para()
            if not in_list or list_type != 'ol':
                flush_list()
                out.append('<ol>')
                in_list = True
                list_type = 'ol'
            out.append(f'<li>{inline(m.group(1))}</li>')
            continue
        # テーブル（簡易）
        if '|' in line and re.match(r'^\|.+\|$', line):
            flush_para(); flush_list()
            cells = [c.strip() for c in line.strip('|').split('|')]
            # 区切り行の検出
            if all(re.match(r'^[-:]+$', c) for c in cells):
                continue  # 区切り行スキップ
            # 簡易表示（thead/tbody判定なし）
            row = '<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>'
            # 直前の出力に応じてtable開閉を調整
            if not out or not out[-1].startswith('<tr>'):
                out.append('<table>' + row)
            else:
                out[-1] += row
            continue
        # 通常段落
        if not in_para:
            in_para = True
        para_buf.append(inline(line))

    flush_para()
    flush_list()
    # tableの閉じタグ補完
    final = '\n'.join(out)
    final = re.sub(r'(<tr>.*?</tr>)(?!<tr>)(?!</table>)', r'\1</table>', final, flags=re.DOTALL)
    final = re.sub(r'(<table>(?:<tr>.*?</tr>)+)(?!</table>)', r'\1</table>', final, flags=re.DOTALL)
    # 簡易閉じ補完
    open_count = final.count('<table>')
    close_count = final.count('</table>')
    final += '</table>' * (open_count - close_count) if open_count > close_count else ''
    return final

# 対象MDファイルをHTMLに変換
md_files = sorted(glob.glob(f"{DRAFTS_MD}/*.md"))
print(f"対象MDファイル: {len(md_files)}件")

drafts_meta = []
for md_path in md_files:
    base = os.path.basename(md_path).replace('.md', '')
    html_path = f"{DRAFTS_HTML}/{base}.html"
    with open(md_path) as f:
        md = f.read()
    # タイトル抽出
    title_m = re.search(r'^#\s+(.+?)$', md, re.MULTILINE)
    title = title_m.group(1) if title_m else base
    title_clean = re.sub(r'\s*申請書ドラフト.*$', '', title)
    # 主体抽出（M or E）
    code_m = re.match(r'\d+_([ME])_', base)
    code = code_m.group(1) if code_m else '?'
    org = 'ミラツク' if code == 'M' else ('esse-sense' if code == 'E' else '?')
    brand = f"GRANT DRAFT — {org}"

    body_html = md_to_html(md)
    body_html += f'\n<div class="footer-mark">ミラツク／esse-sense Grant Schedule 2026 — {org}向けドラフト · 自動生成 · 提出前に内容を要確認</div>'

    rendered = (TEMPLATE
                .replace('__TITLE__', html.escape(title_clean))
                .replace('__BRAND__', html.escape(brand))
                .replace('__CONTENT__', body_html))

    with open(html_path, 'w') as f:
        f.write(rendered)

    drafts_meta.append({
        'filename': f"{base}.html",
        'title': title_clean,
        'org': org,
        'code': code,
        'rank': base.split('_')[0],
        'size': os.path.getsize(html_path),
    })

print(f"HTML生成完了: {len(drafts_meta)}件")
print(f"出力先: {DRAFTS_HTML}")

# index.htmlのDRAFTS配列を更新
import json
index_path = f"{DRAFTS_HTML}/index.html"
with open(index_path) as f:
    idx_html = f.read()

# rank自然順ソート（数字優先 → N100系 → B3xxx系 → B6_xxx名前順）
def sort_key(d):
    r = d['rank']
    if r.isdigit():
        return (0, int(r), d['filename'])
    if r.startswith('N') and r[1:].isdigit():
        return (1, int(r[1:]), d['filename'])
    if r.startswith('B') and len(r) > 1 and r[1:].isdigit():
        return (2, int(r[1:]), d['filename'])
    return (3, r, d['filename'])

drafts_sorted = sorted(drafts_meta, key=sort_key)
draft_lines = [json.dumps(d, ensure_ascii=False) for d in drafts_sorted]
new_array = "const DRAFTS = [\n" + ",\n".join(draft_lines) + "\n];"

# 既存のconst DRAFTS = [ ... ]; を置換
new_html = re.sub(
    r'const DRAFTS = \[.*?\n\];',
    new_array,
    idx_html,
    count=1,
    flags=re.DOTALL,
)
with open(index_path, 'w') as f:
    f.write(new_html)
print(f"index.html更新完了: {len(drafts_sorted)}件")
