from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import pyqtSlot

from GUI.Ui_LibraryChooseDialog import Ui_LibraryChooseDialog


class LibraryChooseDialog(QDialog, Ui_LibraryChooseDialog):
    """Dialog window to asking user for gallery path"""

    directory_path: str = ''

    def __init__(self, dir_path: str, parent=None) -> None:
        """Setup UI objects and window settings"""
        super().__init__(parent)
        self.setupUi(self)
        self.SelectedPathLineEdit.setText(dir_path)

    @pyqtSlot(str, name='on_SelectedPathLineEdit_textChanged')
    def __SelectedPathLineEdit_changed(self, text: str) -> None:
        """Save directory path from LineEdit into"""
        self.directory_path = text

    @pyqtSlot(name='on_BrowseButton_clicked')
    def __BrowseButton_clicked(self) -> None:
        """Open OS's file browse dialog and handle its result"""
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly)
        dialog.exec()

        self.SelectedPathLineEdit.setText(dialog.selectedFiles()[0])

    @pyqtSlot(name='on_ApplyButton_clicked')
    def __ApplyButton_clicked(self) -> None:
        """Accept selected path and close the dialog"""
        self.accept()
