import urllib.request
import re

url = "http://server-test.net/math/download/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('shift_jis', errors='ignore')
        matches = re.findall(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.IGNORECASE | re.DOTALL)
        print(f"Total download links: {len(matches)}")
        for href, text in matches[:30]:
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            print(f"Link: '{clean_text}' -> '{href}'")
except Exception as e:
    print(f"Error: {e}")
