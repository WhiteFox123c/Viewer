import os

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSlot

from GUI.Ui_MainWindow import Ui_MainWindow
from screens.LibraryChooseDialog import LibraryChooseDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main application gallery window"""

    DEFAULT_WINDOW_TITLE: str = 'Empty gallery'

    directory_path: str|None = None

    def __init__(self, parent=None) -> None:
        """Setup UI objects and window settings"""
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowTitle(self.DEFAULT_WINDOW_TITLE)

    def show(self) -> None:
        """Override default show method to check for saved gallery path"""
        super().show()

        if not self.__is_saved_dir_path():
            self.__open_ask_gallery_path_dialog()
        else:
            # TODO: Open saved gallery path...
            print('Open saved gallery folder path')

    def __is_saved_dir_path(self) -> bool:
        """Returns true if the path to the gallery directory was saved at the last launch"""
        return False

    @pyqtSlot(name='on_OpenAction_triggered')
    def __open_ask_gallery_path_dialog(self) -> None:
        """Ask user to select a gallery path"""
        dialog = LibraryChooseDialog(self)
        dialog.exec()

        if dialog.result() == LibraryChooseDialog.DialogCode.Accepted:
            self.__open_path(dialog.directory_path)

    def __set_directory_path(self, directory_path) -> None:
        """Set directory path and window title according to it

        TODO: Save gallery path to the storage
        """
        self.directory_path = directory_path
        self.setWindowTitle(self.DEFAULT_WINDOW_TITLE if directory_path == None else directory_path)

    def __close_current_gallery(self) -> None:
        """Reset gallery path"""
        self.__set_directory_path(None)

    def __open_path(self, directory_path: str) -> None:
        """Open provided gallery path"""
        if (os.path.isdir(directory_path)):
            self.__close_current_gallery()
            self.__set_directory_path(directory_path)
        else:
            message_box = QMessageBox(self)
            message_box.setWindowTitle('Error')
            message_box.setText(f'The gallery folder you specified does not look like a real existing folder\n\n{directory_path}')
            message_box.setIcon(QMessageBox.Icon.Critical)
            message_box.exec()

            self.__open_ask_gallery_path_dialog()
