import sys
from PyQt5.QtWidgets import QApplication
from app.controllers import MainController
from app import load_stylesheet

def main():
    app = QApplication(sys.argv)
    
    # Load and apply the stylesheet
    load_stylesheet(app)
    
    controller = MainController()
    controller.show_main_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
