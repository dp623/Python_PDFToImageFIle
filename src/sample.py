import fitz  # pip install PyMuPDF
import sys
import os

"""
PDFファイルを読み込み、各ページをPNG画像として保存します。

:param pdf_path: 分割するPDFファイルのパス
:param output_folder: 生成されたPNGファイルの保存先フォルダ
"""
def pdf_to_png(pdf_path, output_folder):
    # スクリプトファイルの場所
    workDir = os.path.dirname(os.path.abspath(__file__))

    # PDFファイルを開く
    doc = fitz.open(os.path.join(workDir, pdf_path))

    # 各ページをPNGとして保存
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # ページを読み込む
        pix = page.get_pixmap()  # ピクセルマップを取得
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_folder, f'page_{page_num + 1}.png')
        pix.save(output_path)  # PNGとして保存

    doc.close()  # PDFファイルを閉じる

# メイン
def main():
    # 変換対象
    if len(sys.argv) > 1:
        sourceFile = sys.argv[1]
    else:
        print('\r\nソースファイルが指定されていません。\r\n')
        sys.exit()

    # 結果フォルダ
    resultDirectory = 'result'
    if len(sys.argv) > 2:
        resultDirectory = enumerate(sys.argv)[2]
    
    # 変換実行
    pdf_to_png(sourceFile, resultDirectory)

    # 実行完了メッセージ
    print('\r\n実行完了\r\n')

# 実行
if __name__ == '__main__':
    main()