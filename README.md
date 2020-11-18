# PDFWork
Working with PDF files in Python

There are 4 initial PDF files in this repository - dummy.pdf, wtr.pdf, twopage.pdf and tilt.pdf. The Python file PdfMerger.py uses the modules PyPDF2 and sys to combine all
the PDF files, except wtr.pdf, into 1 single PDF file, named super.pdf. The files appear as different pages of the new file. The file wtr.pdf contains a watermark symbol.
Then, the file MarkAdder.py uses again the module PyPDF2 to put the watermark from wtr.pdf onto each page of the file super.pdf, created earlier. The new creation with all
pages marked by the watermark symbol is saved as TagedPages.pdf file.
