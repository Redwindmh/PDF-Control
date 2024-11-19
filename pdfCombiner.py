from pypdf import PdfWriter

pdf_list = [
    "./pdf_files/ヘンドリックス履歴書.pdf",
    "./pdf_files/ヘンドリックス職務経歴書.pdf",
]


merger = PdfWriter()

for pdf in pdf_list:
    merger.append(pdf)

merger.write("./output/ヘンドリックス履歴書＋職務経歴書.pdf")
merger.close()
