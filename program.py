import os, sys
import ipdb
from image_client import ImageDrawClient
import time


def current_path():
    return os.getcwd() + '/'


def run_image_maker(image_path):
    image_out_path = current_path() + 'output_' + str(int(time.time())) + '.png'

    draw_tool = ImageDrawClient()
    im = draw_tool.open_image(image_path)

    text = "Text"
    im = draw_tool.write_text_on_image(im, 20, 20, text, 20)

    draw_tool.save_image(im, image_out_path)


def cli():
    if len(sys.argv) > 2:
        exit()

    image_name = sys.argv[1]

    im_path = current_path() + image_name 
    
    run_image_maker(im_path)
    


if __name__ == '__main__':
    cli()



