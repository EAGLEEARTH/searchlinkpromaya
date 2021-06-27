import fitz


file = fitz.open('Aktel Collection Katalog 2018-5.pdf')

for pageNumber, page in enumerate(file.pages(), start=1):

    text = page.getText()

    txt = open(f'report_Page_{pageNumber}.txt','a')

    txt.writelines(text)

    txt.close()


for pageNumber, page in enumerate(file.pages(), start=1):

    for imgNumber, img in enumerate(page.getImageList(), start=1):

        xref = img[0]

        pix = fitz.Pixmap(file, xref)

        if pix.n > 4:

            pix = fitz.Pixmap(fitz.csRGB, pix)

        pix.writePNG(f'mage_page{pageNumber}_{imgNumber}.png')    