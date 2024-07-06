import unittest
from PyQt5.QtWidgets import QApplication
from app.vtk import VTKViewer

class TestVTKViewer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.vtk_viewer = VTKViewer()

    def test_initialize_scene(self):
        self.assertIsNotNone(self.vtk_viewer.renderer)

if __name__ == "__main__":
    unittest.main()
