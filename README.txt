=== CLI-toolkit ===
PDFやZIPファイルを楽に取り扱うためのPythonスクリプトです。

-----プログラム-----
- mrg.py    - 複数のPDFファイルを1つにまとめます
- splt.py   - 1つのPDFをページごとに分割して保存します
- cnvrt.py  - SVGファイルをPDFとPNGファイルに変換します
- extrct.py - Windows標準機能では出来ないパスワード付きZIPファイルを解凍します

-----使い方-----
install:   依存関係は [ pip install -r requirements.txt ] で導入してください

mrg.py:    PDFファイルを ./merge に移動し、 [ python mrg.py ]
splt.py:   PDFファイル(1つのみ)を ./split に移動し、 [ python splt.py ]
cnvrt.py:  SVGファイル(1つのみ)を ./svgtopdf に移動し、 [ python cnvrt.py ]
extrct.py: ZIPファイル(1つのみ)を ./exzip に移動し、 [ python extrct.py パスワード ]

-----更新履歴・リポジトリ-----
v1. 20220504 公開
v2. 20220609 依存関係を明示
v3. 20220916 ファイル名を自動取得するように。手動指定の必要は無くなりました

https://github.com/bosshii/cli-toolkit
     


