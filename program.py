import os, sys
import ipdb
from image_client import ImageDrawClient
import time
import ConfigParser
from ast import literal_eval as make_tuple
from csv_client import CsvClient
from pdf_writer import PdfWriter


def current_path(filename):
    return os.getcwd() + '/' + filename


def load_cfg(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(current_path(config_file)))
    return config


def get_markers(config):
    markers = {}
    markers['school'] = make_tuple(config.get('markers', 'school'))
    markers['year'] = make_tuple(config.get('markers', 'year'))
    markers['award'] = make_tuple(config.get('markers', 'award'))
    markers['recipient'] = make_tuple(config.get('markers', 'recipient'))
    return markers


def get_font(config):
    font = {}
    font['color'] = config.get('font', 'color')
    font['name'] = config.get('font', 'name')
    font['size'] = config.getint('font', 'size')
    return font


def get_data(config):
    cc = CsvClient(config.get('csv', 'filename'))
    data = cc.read()
    return data


def write_text(draw_tool, marker, font, text, image):
    pos_x = marker[0]
    pos_y = marker[1]

    image = draw_tool.write_text_on_image(image, pos_x, pos_y, text, font)
    return image


def create_output_folder(folder):
    output_folder = folder + '_' + str(int(time.time()))
    os.makedirs(output_folder)
    return os.path.abspath(output_folder)


def save_image(draw_tool, image, folder):
    image_out_path = folder + '/' + 'image_' + str(int(time.time() * 1000)) + '.png'
    draw_tool.save_image(image, image_out_path)
    return image_out_path


def create_new_pdf(folder, images):
    pdf_creator = PdfWriter(folder + '/' + 'pdf_' + str(int(time.time() * 1000)) + '.pdf')
    for image in images:
        pdf_creator.add_image(image, 687, 809)
    pdf_creator.images_on_pdf()
    pdf_creator.save()


def run_image_maker(image_path):
    config = load_cfg('conf.cfg')
    draw_tool = ImageDrawClient()

    markers = get_markers(config)
    font = get_font(config)
    data = get_data(config)

    school = 'John Scottus'
    year = '2016'

    output_folder = create_output_folder('output')
    pdf_folder = create_output_folder('pdf')

    count = 0
    images = []

    for row in data:
        im = draw_tool.open_image(image_path)
        im = write_text(draw_tool, markers['school'], font, school, im)
        im = write_text(draw_tool, markers['year'], font, year, im)
        im = write_text(draw_tool, markers['award'], font, row['Award'] + ' ' + row['Level'], im)
        im = write_text(draw_tool, markers['recipient'], font, row['Recipient'], im)
        save_file = save_image(draw_tool, im, output_folder)
        count += 1
        images.append(save_file)
        if count % 6 == 0:
            create_new_pdf(pdf_folder, images)
            count == 0
            images == []
    
    # catch stragglers (will replace later ;] )
    create_new_pdf(pdf_folder, images)



def cli():
    if len(sys.argv) > 2:
        exit()

    image_name = sys.argv[1]

    im_path = current_path(image_name)
    
    run_image_maker(im_path)
    


if __name__ == '__main__':
    cli()

