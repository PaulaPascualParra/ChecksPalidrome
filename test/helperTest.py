import unittest
from unittest.mock import patch
from src import helper


class ReadFileTest(unittest.TestCase):
    CORRECT_PATH = "test_files/pretty_text.txt"
    INCORRECT_PATH = "texts.txt"
    PDF_PATH = "test_files/text_pdf.pdf"
    INPUT_TEXT = "abba"

    def test_whenCorrectPath_returnInput(self):
        data = helper.read_file(self.CORRECT_PATH)
        self.assertEqual(self.INPUT_TEXT, data)

    def test_whenIncorrectPath_returnFileNotFound(self):
        self.assertRaises(FileNotFoundError, helper.read_file, self.INCORRECT_PATH)

    def test_whenPdfPath_returnUnicodeDecodeError(self):
        self.assertRaises(UnicodeDecodeError, helper.read_file, self.PDF_PATH)

    # todo: better input
    def test_whenCantRead_returnException(self):
        self.assertRaises(Exception, helper.read_file, self.PDF_PATH)


class ProcessDataTest(unittest.TestCase):
    PROCESS_DATA = "aba"
    UPPERCASE_SPACE_LINE_JUMP_DATA = "A b\na"

    @patch('src.helper.input_process_data', return_value=False)
    def test_whenProcessFalse_returnRawData(self, input):
        self.assertEqual(self.UPPERCASE_SPACE_LINE_JUMP_DATA, helper.process_data(self.UPPERCASE_SPACE_LINE_JUMP_DATA))

    @patch('src.helper.input_process_data', return_value=True)
    def test_whenProcessTrue_returnProcessData(self, input):
        self.assertEqual(self.PROCESS_DATA, helper.process_data(self.UPPERCASE_SPACE_LINE_JUMP_DATA))


if __name__ == '__main__':
    unittest.main()
