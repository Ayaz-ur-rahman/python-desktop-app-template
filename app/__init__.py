import os

def load_stylesheet(app):
    """
    Load and apply the QSS stylesheet to the application.
    """
    qss_path = os.path.join(os.path.dirname(__file__), 'resources', 'styles', 'main.qss')
    with open(qss_path, 'r') as file:
        app.setStyleSheet(file.read())

__all__=["load_stylesheet"]
