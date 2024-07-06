import unittest
from PyQt5.QtWidgets import QApplication
from app.gui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.main_window = MainWindow()

    def test_window_title(self):
        self.assertEqual(self.main_window.windowTitle(), "My VTK Application")

if __name__ == "__main__":
    unittest.main()
