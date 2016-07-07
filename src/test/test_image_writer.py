from image_writer import ImageWriter
from unittest import TestCase


class TestImageWriter(TestCase):
    def test_image_writer(self):
        font = {'name': 'hellvetica',
                'size': 46}
        writer = ImageWriter(font)
        self.assertIsNotNone(writer)

    def test_save_image(self):
        pass

    def test_rotate_image(self):
        pass

    def test_write_text_on_image(self):
        pass
