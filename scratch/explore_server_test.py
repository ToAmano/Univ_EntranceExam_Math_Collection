import urllib.request
import re

url = "http://server-test.net/math/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        html_bytes = response.read()
        
        decoded_html = None
        for encoding in ['shift_jis', 'cp932', 'euc-jp', 'utf-8']:
            try:
                decoded_html = html_bytes.decode(encoding)
                print(f"Decoded using {encoding}")
                break
            except Exception:
                continue

        if decoded_html:
            # href と アンカーテキストの抽出
            matches = re.findall(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', decoded_html, re.IGNORECASE | re.DOTALL)
            print(f"Total links found: {len(matches)}\n")
            for href, text in matches:
                clean_text = re.sub(r'<[^>]+>', '', text).strip()
                if any(k in clean_text or k in href for k in ['東京', '京都', '東工大', 'titech', 'tokyo', 'kyoto']):
                    print(f"Text: '{clean_text}' | Href: '{href}'")

except Exception as e:
    print(f"Error: {e}")
