from unittest import TestCase
from pdf_writer import PdfWriter


class TestPdfWriter(TestCase):
    def test_create_pdf_writer(self):
        filename = 'test_pdf'
        pdf_writer = PdfWriter(filename)
        self.assertIsNotNone(pdf_writer)

