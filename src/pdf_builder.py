from reportlab.platypus import SimpleDocTemplate, Image, Table


class PdfBuilder(object):
    def __init__(self, filename):
        self.filename = filename
        self.elements = []
        self.writer = SimpleDocTemplate(self.filename, pagesize=(1500, 2000),
                                        rightMargin=0, leftMargin=0,
                                        topMargin=0, bottomMargin=0)
        self.images = []

    def add_image(self, image, x, y):
        im = Image(image, x, y)
        self.images.append(im)

    def images_on_pdf(self):
        image_count = len(self.images)
        data = []
        if image_count == 6:
            data = [[self.images[0], self.images[1]],
                    [self.images[2], self.images[3]],
                    [self.images[4], self.images[5]]]
        elif image_count == 5:
            data = [[self.images[0], self.images[1]],
                    [self.images[2], self.images[3]],
                    [self.images[4]]]
        elif image_count == 4:
            data = [[self.images[0], self.images[1]],
                    [self.images[2], self.images[3]]]
        elif image_count == 3:
            data = [[self.images[0], self.images[1]],
                    [self.images[2]]]
        elif image_count == 2:
            data = [[self.images[0], self.images[1]]]
        elif image_count == 1:
            data = [[self.images[0]]]
        t = Table(data, 738, 920)
        self.elements.append(t)

    def save(self):
        self.writer.build(self.elements)

    def compress(self):
        pass
