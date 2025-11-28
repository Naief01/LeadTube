"""
Main entry point for the YouTube Lead Scraper application.
"""
import sys
from PyQt6.QtWidgets import QApplication
from .gui import MainWindow

def main():
    """
    Initializes and runs the PyQt application.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
