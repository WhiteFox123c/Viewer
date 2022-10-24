from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot

from GUI.Ui_MainWindow import Ui_MainWindow
from screens.LibraryChooseDialog import LibraryChooseDialog

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

        if not self.__is_saved_dir_path():
            self.__open_ask_dir_path_modal()
        else:
            pass

    def __is_saved_dir_path(self) -> bool:
        """ Checks if there is saved dir path

        Returns true if dir path is saved from previos launch or not
        """
        return False

    @pyqtSlot(name='on_actionOpen_triggered')
    def __open_ask_dir_path_modal(self) -> None:
        """ Slot for actionOpen on triggered

        Open a modal window to ask user for folder path
        """
        dialog = LibraryChooseDialog(self)
        dialog.exec()
