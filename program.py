import os, sys
import ipdb
from image_client import ImageDrawClient
import time
import ConfigParser
from ast import literal_eval as make_tuple


def current_path(filename):
    return os.getcwd() + '/' + filename


def load_cfg(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(current_path(config_file)))
    return config


def get_markers(config):
    markers = {}
    markers['School'] = make_tuple(config.get('markers', 'school'))
    markers['Year'] = make_tuple(config.get('markers', 'year'))
    markers['Award'] = make_tuple(config.get('markers', 'award'))
    markers['Recipient'] = make_tuple(config.get('markers', 'recipient'))
    return markers


def get_font(config):
    font = {}
    font['color'] = config.get('font', 'color')
    font['name'] = config.get('font', 'name')
    font['size'] = config.getint('font', 'size')
    return font


def write_text(draw_tool, marker, font, text, image):
    pos_x = marker[0]
    pos_y = marker[1]

    image = draw_tool.write_text_on_image(image, pos_x, pos_y, text, font)
    return image


def run_image_maker(image_path):
    out_file_name = 'output_' + str(int(time.time())) + '.png'
    image_out_path = current_path(out_file_name)

    config = load_cfg('conf.cfg')

    draw_tool = ImageDrawClient()
    im = draw_tool.open_image(image_path)


    markers = get_markers(config)
    font = get_font(config)
    text = "Text"

    for marker, marker_pos in markers.iteritems():
        im = write_text(draw_tool, marker_pos, font, text, im)

    draw_tool.save_image(im, image_out_path)



def cli():
    if len(sys.argv) > 2:
        exit()

    image_name = sys.argv[1]

    im_path = current_path(image_name)
    
    run_image_maker(im_path)
    


if __name__ == '__main__':
    cli()



