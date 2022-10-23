import sys

import resources.theme.resources

from PyQt6.QtCore import QFile, QTextStream
from PyQt6.QtWidgets import QApplication
import darkdetect

from screens.MainWindow import MainWindow


def start_application() -> None:
    """ Starts the aplication

    Create main window, set a theme according to OS theme
    and open it
    """

    app = QApplication(sys.argv)

    file = QFile(':/theme/{}/stylesheet.qss'
            .format('dark' if darkdetect.isDark() else 'light'))
    file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    start_application()
