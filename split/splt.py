import PyPDF2
import glob

filename = "".join(glob.glob('*.pdf'))
src_pdf = PyPDF2.PdfFileReader(filename)
for i in range(src_pdf.numPages):
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(i))
    with open('{}_{}.pdf'.format(filename.replace('.pdf', '').replace('.PDF', ''), i+1), 'wb') as f:
        dst_pdf.write(f)



