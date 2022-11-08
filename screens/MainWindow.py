import os

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSlot

from GUI.Ui_MainWindow import Ui_MainWindow
from screens.LibraryChooseDialog import LibraryChooseDialog
from config.GalleryConfig import GalleryConfig

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
            dialog_result = self.__open_ask_gallery_path_dialog()
            if dialog_result['accepted'] == True:
                self.__open_path(dialog_result['path'])
        else:
            self.__open_path(self.__get_saved_dir_path())

    @pyqtSlot(name='on_CloseAction_triggered')
    def __closeAction_triggered(self) -> None:
        """Closing opened directory and show an empty gallery"""
        self.__set_directory_path(None)

    def __is_saved_dir_path(self) -> bool:
        """Returns true if the path to the gallery directory was saved at the last launch"""
        if os.path.isfile(f'{os.getcwd()}/{GalleryConfig.SAVE_GALLERY_PATH}') and len(self.__get_saved_dir_path()) > 0:
            return True

        return False

    def __get_saved_dir_path(self) -> str:
        """Returns first line from SAVE_GALLERY_PATH file"""
        with open(f'{os.getcwd()}/{GalleryConfig.SAVE_GALLERY_PATH}', 'r') as file:
            return file.readline()

    @pyqtSlot(name='on_OpenAction_triggered')
    def __openAction_triggered(self):
        dialog_result = self.__open_ask_gallery_path_dialog()
        if dialog_result['accepted'] == True:
            self.__open_path(dialog_result['path'])

    def __open_ask_gallery_path_dialog(self) -> dict:
        """Ask user to select a gallery path"""
        dialog = LibraryChooseDialog(self)
        dialog.exec()

        return {
            'accepted': dialog.result() == LibraryChooseDialog.DialogCode.Accepted,
            'path': dialog.directory_path
        }

    def __set_directory_path(self, directory_path) -> None:
        """Set directory path and window title according to it"""
        self.directory_path = directory_path
        self.setWindowTitle(self.DEFAULT_WINDOW_TITLE if directory_path == None else directory_path)

        with open(f'{os.getcwd()}/{GalleryConfig.SAVE_GALLERY_PATH}', 'w+') as file:
            file.write('' if directory_path == None else directory_path)

    def __chosen_dir_incorrect(self, directory_path):
        message_box = QMessageBox(self)
        message_box.setWindowTitle('Error')
        message_box.setText(f'The gallery folder you specified does not look like a real existing folder\n\n{directory_path}')
        message_box.setIcon(QMessageBox.Icon.Critical)
        message_box.exec()

    def __open_path(self, directory_path: str) -> None:
        """Open provided gallery path"""
        if not os.path.isdir(directory_path):
            self.__chosen_dir_incorrect(directory_path)
            return

        self.__set_directory_path(directory_path)
        with os.scandir(self.directory_path) as _:
            for entry in _:
                if (entry.is_file and entry.name.endswith(GalleryConfig.IMAGES_EXT)):
                    pass
