import os
import sys
import glob
import shutil

sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.join(os.path.dirname(__file__), '..'))

from tex_to_md import convert_tex_clean

TARGETS = [
    "src/titech/kouki/1996/1/solution.tex",
    "src/titech/kouki/1997/2/solution.tex",
    "src/titech/kouki/1998/2/solution.tex",
    "src/titech/kouki/1999/2/solution.tex",
    "src/titech/kouki/2006/1/solution.tex",
    "src/titech/zenki/1962/4/solution.tex",
    "src/titech/zenki/1963/3/solution.tex",
    "src/ukyoto/kouki/1995/6/solution.tex",
    "src/ukyoto/kouki/1997/3/solution.tex",
    "src/utokyo/kouki/1990/3/solution.tex",
    "src/utokyo/kouki/1992/1/solution.tex",
    "src/utokyo/kouki/1999/3/solution.tex",
    "src/utokyo/kouki/2005/1/solution.tex",
    "src/utokyo/kouki/2006/2/solution.tex",
]

out_root = "scratch/test_sweep_out"
if os.path.exists(out_root):
    shutil.rmtree(out_root)
os.makedirs(out_root, exist_ok=True)

results = {}
for tex_path in TARGETS:
    if not os.path.exists(tex_path):
        print(f"SKIP (missing): {tex_path}")
        continue
    name = tex_path.replace('/', '_')
    svg_dir = os.path.join(out_root, name, "svg")
    md_path = os.path.join(out_root, name, "out.md")
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    print(f"\n=== {tex_path} ===")
    try:
        convert_tex_clean(tex_path, md_path, {}, "/images/tikz/test", svg_dir)
    except Exception as e:
        print(f"  EXCEPTION: {e}")
        results[tex_path] = "EXCEPTION"
        continue
    svgs = glob.glob(os.path.join(svg_dir, "*.svg"))
    n_expected = None
    results[tex_path] = f"{len(svgs)} svg(s) produced"

print("\n\n===== SUMMARY =====")
for k, v in results.items():
    print(f"{k}: {v}")
