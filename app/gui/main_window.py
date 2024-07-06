from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .widgets import VTKWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My VTK Application")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.vtk_widget = VTKWidget()
        layout.addWidget(self.vtk_widget)

        self.setCentralWidget(central_widget)
