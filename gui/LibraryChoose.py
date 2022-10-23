import os

from PyQt6 import QtWidgets

from tkinter import filedialog

from gui.templates.Ui_LibraryChoose import Ui_LibraryChoose


class LibraryChoose(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LibraryChoose, self).__init__(parent)
        self.ui = Ui_LibraryChoose()
        self.ui.setupUi(self)
        self.__register_handlers()

    def __register_handlers(self):
        self.ui.chooseButton.clicked.connect(self.__action_choose_library_button_handler)
        self.ui.okButton.clicked.connect(self.__path_check)

    def __action_choose_library_button_handler(self):
        self.ui.lineEdit.setText(filedialog.askdirectory())

    def get_path(self):
        return self.ui.lineEdit.text()

    def __path_check(self):
        if os.path.exists(self.get_path()):
            self.setResult(QtWidgets.QDialog.DialogCode.Accepted)
            self.close()
        else:
            self.ui.lineEdit.setPlaceholderText("Ты долбоеб!")