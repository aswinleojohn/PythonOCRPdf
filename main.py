#pypdf does what I expect in this area. Using the following script:

#!/usr/bin/python
#

from PyPDF2 import PdfFileWriter, PdfFileReader

with open("/Users/leojohnashwin/pythonpdf/data.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    #print "document has %s pages." % numPages

    for i in range(numPages):
        page = input1.getPage(i)
        #print page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y()
        page.trimBox.lowerLeft = (413, 413)
        page.trimBox.upperRight =(555, 500)
        print(page.cropBox.getUpperLeft())
        print(page.cropBox.getUpperRight())
        print(page.cropBox.getLowerLeft())
        print(page.cropBox.getLowerRight())
        #page.cropBox.upperLeft = (400, 200)
        page.cropBox.upperRight = (555, 500)
        page.cropBox.lowerLeft = (413, 413)
        #page.cropBox.lowerRight = (555, 400)
        print(type(page))
        output.addPage(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)
