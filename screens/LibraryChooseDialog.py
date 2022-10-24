from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import pyqtSlot

from GUI.Ui_LibraryChooseDialog import Ui_LibraryChooseDialog

class LibraryChooseDialog(QDialog, Ui_LibraryChooseDialog):
    """ Modal window

    Window for ask to select a folder with target files
    """

    def __init__(self, parent=None) -> None:
        """ Initialize a window

        Setup ui objects and window settings
        """
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_BrowseButton_clicked(self) -> None:
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly)
        dialog.exec()

        self.directory_path = dialog.selectedFiles()[0]
        self.SelectedPathLineEdit.setText(self.directory_path)

    @pyqtSlot()
    def on_ApplyButton_clicked(self) -> None:
        self.setResult(QtWidgets.QDialog.DialogCode.Accepted)
        self.close()
