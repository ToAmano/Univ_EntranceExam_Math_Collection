# 問題別 OGP 画像

`scratch/generate_problem_ogp.py` は `scratch/tex_to_md.py` が作った問題文 Markdown と、対応する `fig_problem_*.svg` の先頭の図から 1200×630 px の PNG を作る。解答本文や `fig_*.svg` は画像に使わない。原稿の TeX は変更しない。

ローカルでは TeX→Markdown 変換後、次のコマンドで生成する。Python には Pillow、システムには LuaLaTeX、`pdftocairo`、`rsvg-convert` が必要。

```sh
python3 scratch/generate_problem_ogp.py
```

画像は `web/public/ogp/problems/` に保存する。各問題の Markdown、図の SVG、生成器の版をハッシュ化した `manifest.json` を同じディレクトリに置き、入力が変わらなければ次回の生成を省略する。画像は Git 管理せず、Pages の GitHub Actions では `actions/cache` から復元する。初回またはキャッシュ消失後は全問を再生成する。

各画像は問題文の先頭から、数式の途中を避けて短い抜粋を載せる。長い別行立ての数式は「（数式）」と示す。入り切らない場合は抜粋を短くして再試行し、それでも描画できない問題は共通 OGP 画像を使う。生成器は `generated`、`cached`、`fallback`、`failed` の件数を表示する。`fallback` は定型文カードを生成した件数、`failed` は画像が無く共通画像へ戻る件数。サイトは問題別 PNG が存在するページだけそれを `og:image` と `twitter:image` に指定する。

試行時は `--limit 40 --output /tmp/problem-ogp-check` などで対象数と出力先を限定できる。全体生成後は `du -sh web/public/ogp/problems` で容量を確認する。Pages のビルド後には `scratch/check_site_size.py web/dist` が総容量を表示し、900 MB 超で警告、1,000 MB 超で失敗する。
