from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Image, Table


class PdfWriter(object):

    def __init__(self, filename):
        self.filename = filename
        self.elements = []
        self.writer = SimpleDocTemplate(self.filename, pagesize=(1500, 2000), 
						rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)
        self.images = []


    def add_image(self, image, x, y):
        im = Image(image, x, y)
        self.images.append(im)
        # self.elements.append(im)

   
    def images_on_pdf(self):
        data = [[self.images[0], self.images[1]],
                [self.images[2], self.images[3]]]

        t = Table(data,738,920)
        self.elements.append(t)


    def save(self):
        self.writer.build(self.elements)

