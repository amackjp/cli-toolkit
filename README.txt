=== CLI-toolkit ===
PDFやZIPファイルを楽に取り扱うためのPythonスクリプトです

mrg.pyは複数のPDFを一つのファイルにまとめ、splt.pyは逆にページごとに分割し、cnvrt.pyはSVGファイルをPDFとPNGファイルに変換します
extrct.pyはWindows標準機能では出来ないパスワード付ZIPファイルの解凍を行います

-----programs-----
- mrg.py    - merge several PDF files to 1 file
- splt.py   - split by each pages
- cnvrt.py  - convert svg file to pdf and png
- extrct.py - extract zip with password

-------usage------
install:   run [ pip install -r requirements.txt ]

mrg.py:    move PDFs to ../merge 
           run [ python mrg.py ]
splt.py:   move PDF to ../split
           run [ python splt.py ]
cnvrt.py:  move SVG to ../svgtopdf
           run [ python cnvrt.py SVGfilename.svg ]
extrct.py: move ZIP to ../exzip
           run [ python extrct.py ZIPfilename.zip password ]

-----repository----
https://github.com/amackjp/cli-toolkit
     


