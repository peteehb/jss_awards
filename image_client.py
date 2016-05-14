from PIL import ImageFont, ImageDraw, Image


class ImageDrawClient():

    def __init__(self):
        pass

    def open_image(self, path):
        im = Image.open(path)
        return im

    def save_image(self, im, path):
        try:
            im.save(path)
        except Exception, e:
            print e
        

    def rotate_image(self, im, degrees):
        im.rotate(degrees)
        return im

    def write_text_on_image(self, im, x, y, text, font):
        draw = ImageDraw.Draw(im)

        # use a bitmap font
        #font = ImageFont.loag("arial.pil")
        #draw.text((x, y), text, font=font)

        # using a truetype font
        # raise Exception(font['name'], font['size'])
        open_font = ImageFont.truetype(font['name'], font['size'])

        draw.text((x, y), text, font=open_font, fill=(0,0,0))
        return im

