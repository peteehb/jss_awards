from PIL import ImageFont, ImageDraw, Image


class ImageCreator(object):
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

    def write_text_on_image(self, im, height, text, font):
        draw = ImageDraw.Draw(im)
        font_txt = ImageFont.truetype(font['name'], font['size'])
        w, h = draw.textsize(text, font=font_txt)
        W = im.width
        draw.text(((W - w) / 2, height), text, font=font_txt,
                  fill=(42, 60, 123))
        return im