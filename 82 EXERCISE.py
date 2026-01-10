from pypdf import PdfWriter
import os
merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("100 special half yearly.pdf")
merger.close()