from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot

from GUI.Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """ Main application window

    Window with gallery list and common controls
    """

    def __init__(self, parent=None) -> None:
        """ Initialize a window

        Setup ui objects and window settings
        """
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_actionOpen_triggered(self) -> None:
        """ Slot for actionOpen on triggered

        Ask user to select a folder with target files
        """
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly)
        dialog.exec()
