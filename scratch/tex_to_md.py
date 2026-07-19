# scratch/tex_to_md.py
import os
import re
import subprocess
import sys

def preprocess_latex(content):
    # \bm{x} ➔ \mathbf{x}
    content = re.sub(r'\\bm\{([^}]+)\}', r'\\mathbf{\1}', content)
    # \R ➔ \mathbb{R}
    content = re.sub(r'\\R(?![a-zA-Z])', r'\\mathbb{R}', content)
    content = re.sub(r'\\C(?![a-zA-Z])', r'\\mathbb{C}', content)
    content = re.sub(r'\\N(?![a-zA-Z])', r'\\mathbb{N}', content)
    content = re.sub(r'\\Z(?![a-zA-Z])', r'\\mathbb{Z}', content)
    content = re.sub(r'\\Q(?![a-zA-Z])', r'\\mathbb{Q}', content)
    return content

def convert_tex_to_md(tex_path, output_md_path, frontmatter):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    processed_content = preprocess_latex(content)
    
    # テンポラリファイルを作成
    temp_tex = tex_path + ".temp.tex"
    with open(temp_tex, 'w', encoding='utf-8') as f:
        f.write(processed_content)
        
    try:
        # Pandocを走らせてMarkdownへ変換
        cmd = ["pandoc", temp_tex, "-t", "markdown", "--mathjax"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        md_body = result.stdout
    finally:
        if os.path.exists(temp_tex):
            os.remove(temp_tex)

    # Frontmatterを付与して保存
    fm_str = "---\n"
    for k, v in frontmatter.items():
        fm_str += f"{k}: \"{v}\"\n"
    fm_str += "---\n\n"
    
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(fm_str + md_body)

def process_all_src():
    src_root = "src"
    dest_root = "web/src/content/solutions"
    
    for root, _, files in os.walk(src_root):
        for file in files:
            if file in ("problem.tex", "solution.tex"):
                parts = os.path.normpath(root).split(os.sep)
                if len(parts) >= 5: # src/todai/zenki/1990/1
                    uni, category, year, q_num = parts[1], parts[2], parts[3], parts[4]
                    type_str = "problem" if file == "problem.tex" else "solution"
                    
                    output_name = f"{uni}-{category}-{year}-{q_num}-{type_str}.md"
                    output_path = os.path.join(dest_root, output_name)
                    
                    fm = {
                        "university": uni,
                        "category": category,
                        "year": year,
                        "question": q_num,
                        "type": type_str,
                        "title": f"{uni.upper()} {year} {category} Q{q_num} ({type_str})"
                    }
                    
                    tex_file_path = os.path.join(root, file)
                    try:
                        convert_tex_to_md(tex_file_path, output_path, fm)
                    except Exception as e:
                        print(f"Error converting {tex_file_path} to {output_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    process_all_src()
