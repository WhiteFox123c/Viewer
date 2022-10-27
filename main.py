import sys

import resources.themes.themes

from PyQt6.QtCore import QFile, QTextStream
from PyQt6.QtWidgets import QApplication
import darkdetect

from screens.MainWindow import MainWindow


def set_theme(app: QApplication):
    file = QFile(':/theme/{}/stylesheet.qss'
            .format('dark' if darkdetect.isDark() else 'light'))
    file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())


def start_application() -> None:
    app = QApplication(sys.argv)

    set_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    start_application()
