import unittest
import mock
import file_operation

from StringIO import StringIO

class FileTest(unittest.TestCase):
    def test_baba(self):
        with mock.patch("os.path.exists") as mock_exists:
            mock_exists.return_value = False
            self.assertRaises(Exception, lambda: file_operation.baba("test.txt"))

    def test_file_write(self):
        with mock.patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            with mock.patch("__builtin__.open") as mock_open:
                mock_open.return_value = StringIO()
                mock_open.return_value.close = lambda: None
                file_operation.baba("test.txt")
                self.assertEqual(mock_open.return_value.getvalue(), "test")




if __name__ == "__main__":
    unittest.main()
