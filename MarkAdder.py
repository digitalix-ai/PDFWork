import PyPDF2

reader = PyPDF2.PdfFileReader(open("super.pdf",'rb'))

sup_reader = PyPDF2.PdfFileReader(open("wtr.pdf",'rb'))

writer = PyPDF2.PdfFileWriter()

for num in range(reader.getNumPages()):
    page = reader.getPage(num)
    add_page = sup_reader.getPage(0)
    page.mergePage(add_page)
    writer.addPage(page)

with open('TagedPages.pdf', 'wb') as f:
    writer.write(f)