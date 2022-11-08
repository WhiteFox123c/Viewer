import os.path

from PyQt6.QtCore import pyqtSlot
from PyQt6 import QtWidgets

from gui.templates.Ui_MainWindow import Ui_MainWindow
from gui import LibraryChoose


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__saved_path_check()

    def __saved_path_check(self):
        if self.__is_saved_path():
            pass
        else:
            self.__ask_for_path()

    # TODO: Real checking...
    def __is_saved_path(self):
        return False

    def __ask_for_path(self):
        dialog = LibraryChoose.LibraryChoose(self)
        dialog_result = dialog.exec()
        print(dialog_result)
        if dialog_result == QtWidgets.QDialog.DialogCode.Accepted:
            print(dialog.get_path())
        elif dialog_result == QtWidgets.QDialog.DialogCode.Rejected:
            pass

    @pyqtSlot()
    def on_openAction_triggered(self) -> None:
        self.__ask_for_path()
