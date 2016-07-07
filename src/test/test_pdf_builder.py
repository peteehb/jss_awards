from unittest import TestCase
from pdf_builder import PdfBuilder
from reportlab.platypus import SimpleDocTemplate


class TestPdfBuilder(TestCase):
    def test_create_pdf_builder(self):
        filename = 'test_pdf'
        pdf_builder = PdfBuilder(filename)
        self.assertIsNotNone(pdf_builder)
        self.assertIsNotNone(pdf_builder.writer)
        self.assertIsInstance(pdf_builder.writer, SimpleDocTemplate)

    def test_add_image(self):
        filename = 'test_pdf'
        pdf_writer = PdfBuilder(filename)
        pdf_writer.add_image()

    def images_on_pdf(self):
        pass

    def test_save(self):
        pass

    def test_compress(self):
        pass
