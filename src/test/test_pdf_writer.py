from unittest import TestCase
from pdf_writer import PdfBuilder
from reportlab.platypus import SimpleDocTemplate


class TestPdfWriter(TestCase):
    def test_create_pdf_writer(self):
        filename = 'test_pdf'
        pdf_writer = PdfBuilder(filename)
        self.assertIsNotNone(pdf_writer)
        self.assertIsNotNone(pdf_writer.writer)
        self.assertIsInstance(pdf_writer.writer, SimpleDocTemplate)

    def test_add_image(self):
        filename = 'test_pdf'
        pdf_writer = PdfBuilder(filename)
        pdf_writer.add_image()


