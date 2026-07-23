import urllib.request
import re

url = "http://server-test.net/math/php.php?name=tokyo&v1=1&v2=2000&v3=1&v4=5&y=2000&n=5"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as resp:
    html_bytes = resp.read()

html = None
for enc in ['shift_jis', 'cp932', 'euc-jp', 'utf-8']:
    try:
        html = html_bytes.decode(enc)
        break
    except Exception:
        continue

print("=== 取得した HTML 内の主要テキスト/画像/MathJax/TeX ===")
print(html[:2000])

# HTML 内の主要コンテンツ領域を抽出
print("\n=== Body/Question Text ===")
# タグ除去した生の文章
text_clean = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)
text_clean = re.sub(r'<style.*?>.*?</style>', '', text_clean, flags=re.DOTALL)
text_clean = re.sub(r'<[^>]+>', ' ', text_clean)
text_clean = re.sub(r'\s+', ' ', text_clean)
print(text_clean[:1500])
