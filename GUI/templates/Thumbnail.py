from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QToolButton


class Thumbnail(QToolButton):

    origin_path: str
    pixmap: QPixmap

    def __init__(self, parent, path, width):
        super().__init__(parent)
        self.pixmap = QPixmap(path)
        self.setScaledIcon(width)
        self.origin_path = path

    def setScaledIcon(self, width):
        scaled_pixmap = self.pixmap.scaledToWidth(width)
        size = QSize(width, scaled_pixmap.height())
        self.setFixedSize(size)
        self.setIconSize(size)
        self.setIcon(QIcon(scaled_pixmap))
