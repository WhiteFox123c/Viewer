from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QToolButton


class Thumbnail(QToolButton):
    origin_path = None
    size: QSize

    def __init(self, parent):
        super().__init__(parent)

    def create_thumbnail(self, size: QSize, path):
        self.setFixedSize(size)
        self.setIconSize(size)
        self.setIcon(QIcon(QPixmap(path).scaledToWidth(size.width())))
        self.setOriginPath(path)

    def setSize(self, size: QSize):
        self.size = size

    def setOriginPath(self, path):
        self.origin_path = path

