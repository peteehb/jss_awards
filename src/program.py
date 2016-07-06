from image_creator import ImageWriter
from csv_reader import CsvReader
from pdf_writer import PdfBuilder

import utils


def create_new_pdf(folder, images):
    filename = folder + '/' + 'pdf_' + utils.timestamp() + '.pdf'
    pdf_creator = PdfBuilder(filename)
    for image in images:
        pdf_creator.add_image(image, 687, 809)
    pdf_creator.images_on_pdf()
    pdf_creator.save()


def run():
    config = utils.load_cfg('conf.cfg')
    template_path = config.get('image', 'filename')

    markers = {'school': config.getint('markers', 'school'),
               'year': config.getint('markers', 'year'),
               'level': config.getint('markers', 'level'),
               'award': config.getint('markers', 'award'),
               'recipient': config.getint('markers', 'recipient')}

    font = {'color': config.get('font', 'color'),
            'name': config.get('font', 'name'),
            'size': config.getint('font', 'size')}

    images_per_pdf = config.getint('pdf', 'images_per_pdf')
    if images_per_pdf > 6:
        # 6 is the maximum allowed number of images per pdf
        exit()

    csv_file = config.get('csv', 'filename')
    cc = CsvReader(csv_file)
    csv_data = cc.read()

    school = 'John Scottus School'
    year = '2016'

    image_folder = utils.create_folder('images')
    pdf_folder = utils.create_folder('pdfs')

    count = 0
    images = []

    draw_tool = ImageWriter(font)

    for row in csv_data:
        im = draw_tool.open_image(template_path)
        im = draw_tool.write_text(im, markers['school'], school)
        im = draw_tool.write_text(im, markers['year'], year)
        im = draw_tool.write_text(im, markers['level'], row['Level'])
        im = draw_tool.write_text(im, markers['award'], row['Award'])
        im = draw_tool.write_text(im, markers['recipient'], row['Recipient'])
        im_path = image_folder + '/' + 'image_' + utils.timestamp() + '.png'
        draw_tool.save_image(im, im_path)
        count += 1
        images.append(im_path)

        if count % images_per_pdf == 0:
            create_new_pdf(pdf_folder, images)
            count = 0
            images = []

    create_new_pdf(pdf_folder, images)


if __name__ == '__main__':
    run()
