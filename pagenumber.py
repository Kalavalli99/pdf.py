import reportlab
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
 
from PyPDF2 import PdfFileWriter, PdfFileReader

def createPagePdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1,num+1): 
        c.drawString((210//2)*mm, (4)*mm, str(i))
        c.showPage()
    c.save()
    return 
    with open(tmp, 'rb') as f:
        pdf = PdfFileReader(f)
        layer = pdf.getPage(0)
    return layer


if __name__ == "__main__":
    pass
    import sys,os
    path = 'lab.pdf'
#    path = '1.pdf'
    if len(sys.argv) == 1:
        if not os.path.isfile(path):
            sys.exit(1)
    else:
        path = sys.argv[1]
    base = os.path.basename(path)
    
    
    tmp = "__tmp.pdf"
    
    batch = 10
    batch = 0
    output = PdfFileWriter()
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f,strict=False)
        n = pdf.getNumPages()
        if batch == 0:
            batch = -n
        createPagePdf(n,tmp)
        if not os.path.isdir('pdfWithNumbers/'):
            os.mkdir('pdfWithNumbers/')
        with open(tmp, 'rb') as ftmp:
            numberPdf = PdfFileReader(ftmp)
            for p in range(n):
                if not p%batch and p:
                    newpath = path.replace(base, 'pdfWithNumbers/'+ base[:-4] + '_page_%d'%(p//batch) + path[-4:])
                    with open(newpath, 'wb') as f:
                        output.write(f)
                    output = PdfFileWriter()
#                sys.stdout.write('\rpage: %d of %d'%(p, n))
                print('page: %d of %d'%(p, n))
                page = pdf.getPage(p)
                numberLayer = numberPdf.getPage(p)
                
                page.mergePage(numberLayer)
                output.addPage(page)
            if output.getNumPages():
                newpath = path.replace(base, 'pdfWithNumbers/' + base[:-4] + '_page_%d'%(p//batch + 1)  + path[-4:])
                with open(newpath, 'wb') as f:
                    output.write(f)
    
        os.remove(tmp)
