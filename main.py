import fitz

file = fitz.open("pdf/BOYLESTAD Electronic Devices and Circuit Theory.pdf")

#for pageNumber, page in enumerate(file.pages(), start = 1):
#    text = page.getText()
#    txt = open(f'report_Page_{pageNumber}.txt', 'a')
#    txt.writelines(text)
#    txt.close()

for pageNumber, page in enumerate(file.pages(), start = 1):
    for imgNumber, img in enumerate(page.getImageList(), start = 1):
        xref = img[0]
        pix = fitz.Pixmap(file, xref)
        if pix.n < 5:
        #if pix.n - pix.alpha < 4:
        #if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)

        pix.writePNG(f'image_Page{pageNumber}_{imgNumber}.png')