from PIL import ImageFont, ImageDraw, Image


class ImageWriter(object):
    def __init__(self, font):
        self.font = font

    def open_image(self, path):
        im = Image.open(path)
        return im

    def save_image(self, im, path):
        # Improve exception handling
        try:
            im.save(path)
        except Exception, e:
            print e


    def rotate_image(self, im, degrees):
        im.rotate(degrees)
        return im

    def write_text(self, im, height, text):
        draw = ImageDraw.Draw(im)
        font_txt = ImageFont.truetype(self.font['name'], self.font['size'])
        w, h = draw.textsize(text, font=font_txt)
        W = im.width
        draw.text(((W - w) / 2, height), text, font=font_txt,
                  fill=(42, 60, 123))
        return im
