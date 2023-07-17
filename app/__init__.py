import sys
from PyQt6.QtWidgets import QApplication

from app.widgets.main import MainWindow

app = QApplication(sys.argv)
main_window = MainWindow()