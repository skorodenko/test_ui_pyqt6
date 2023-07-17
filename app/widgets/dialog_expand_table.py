from PyQt6.QtWidgets import QDialog
from app.ui.ui_dialog_expand_table import Ui_Dialog


class DialogExpandTable(QDialog, Ui_Dialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.label.setText(text)
