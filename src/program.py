from image_creator import ImageCreator
from csv_reader import CsvReader
from pdf_writer import PdfWriter

import utils


def get_markers(config):
    markers = {'school': config.getint('markers', 'school'),
               'year': config.getint('markers', 'year'),
               'level': config.getint('markers', 'level'),
               'award': config.getint('markers', 'award'),
               'recipient': config.getint('markers', 'recipient')}
    return markers


def get_font(config):
    font = {'color': config.get('font', 'color'),
            'name': config.get('font', 'name'),
            'size': config.getint('font', 'size')}
    return font


def get_csv_data(config):
    cc = CsvReader(config.get('csv', 'filename'))
    data = cc.read()
    return data


def write_text(draw_tool, height, font, text, image):
    image = draw_tool.write_text_on_image(image, height, text, font)
    return image


def save_image(draw_tool, image, folder):
    image_out_path = folder + '/' + 'image_' + utils.timestamp() + '.png'
    draw_tool.save_image(image, image_out_path)
    return image_out_path


def create_new_pdf(folder, images):
    filename = folder + '/' + 'pdf_' + utils.timestamp() + '.pdf'
    pdf_creator = PdfWriter(filename)
    for image in images:
        pdf_creator.add_image(image, 687, 809)
    pdf_creator.images_on_pdf()
    pdf_creator.save()


def run():
    config = utils.load_cfg('conf.cfg')
    image_path = config.get('image', 'filename')

    markers = get_markers(config)
    font = get_font(config)
    data = get_csv_data(config)

    school = 'John Scottus School'
    year = '2016'

    output_folder = utils.create_folder('output')
    pdf_folder = utils.create_folder('pdf')

    count = 0
    images = []

    draw_tool = ImageCreator()

    for row in data:
        im = draw_tool.open_image(image_path)
        im = write_text(draw_tool, markers['school'], font, school, im)
        im = write_text(draw_tool, markers['year'], font, year, im)
        im = write_text(draw_tool, markers['level'], font, row['Level'], im)
        im = write_text(draw_tool, markers['award'], font, row['Award'], im)
        im = write_text(draw_tool, markers['recipient'], font,
                        row['Recipient'], im)
        save_file = save_image(draw_tool, im, output_folder)
        count += 1
        images.append(save_file)
        if count % 4 == 0:
            create_new_pdf(pdf_folder, images)
            count = 0
            images = []

    # catch stragglers (will replace later ;] )
    images.append(images[0])
    images.append(images[0])
    images.append(images[0])
    create_new_pdf(pdf_folder, images)


if __name__ == '__main__':
    run()
