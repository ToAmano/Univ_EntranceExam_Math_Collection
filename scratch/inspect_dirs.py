import os

dirs = {
    "Math-Solutions": "/Users/amano/works/research/Math-Solutions",
    "titech_kouki": "/Users/amano/works/research/titech_kouki",
    "homepage_solutions": "/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions"
}

def print_tree(path, max_depth=4, current_depth=0, indent=""):
    if current_depth > max_depth:
        return
    try:
        items = sorted(os.listdir(path))
    except Exception as e:
        print(f"{indent}[Error reading: {e}]")
        return
    
    # 隠しファイルやGit、history、node_modules等は除外
    ignored = {".git", ".gitignore", ".DS_Store", ".history", "node_modules", "__pycache__"}
    items = [item for item in items if item not in ignored]
    
    for item in items:
        full_path = os.path.join(path, item)
        is_dir = os.path.isdir(full_path)
        
        if is_dir:
            # サブディレクトリ内の全ファイル数をカウント (隠しファイル除く)
            num_files = 0
            for root, _, files in os.walk(full_path):
                num_files += len([f for f in files if not f.startswith(".")])
            print(f"{indent}📁 {item}/ (contains {num_files} files)")
            # 階層が深すぎる場合はこれ以上潜らないようにするが、ファイル数が多くてディレクトリ自体が多い場合は制限
            # 特定のサブフォルダ内が年度だらけなら、年度の一覧を簡略化するなどの処理を入れる
            sub_items = [si for si in os.listdir(full_path) if si not in ignored]
            if all(os.path.isdir(os.path.join(full_path, si)) and si.isdigit() for si in sub_items if not si.startswith(".")):
                # すべてが数値（年度）のディレクトリの場合、詳細を掘り下げずに概要だけ表示する
                years = sorted([int(si) for si in sub_items if si.isdigit()])
                if years:
                    print(f"{indent}    ℹ️ Years: {years[0]} - {years[-1]} (Total {len(years)} years)")
            else:
                print_tree(full_path, max_depth, current_depth + 1, indent + "    ")
        else:
            size_kb = os.path.getsize(full_path) / 1024
            print(f"{indent}📄 {item} ({size_kb:.1f} KB)")

for name, path in dirs.items():
    print("=" * 80)
    print(f"Directory: {name} ({path})")
    print("=" * 80)
    print_tree(path, max_depth=4)
    print("\n")
