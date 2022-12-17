from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QToolButton
from functions.getDominantColour import getDominantColour


class Thumbnail(QToolButton):

    origin_path: str
    pixmap: QPixmap
    source_size: QSize
    dominant_colour: int | None = None

    def __init__(self, parent, path, width):
        super().__init__(parent)
        self.pixmap = QPixmap(path)
        self.source_size = self.pixmap.size()
        if self.pixmap.width() > self.pixmap.height():
            if self.pixmap.width() > 1280:
                self.pixmap = self.pixmap.scaledToWidth(1280)
        else:
            if self.pixmap.height() > 1280:
                self.pixmap = self.pixmap.scaledToHeight(1280)
        self.setScaledIcon(width)
        self.origin_path = path

    def setScaledIcon(self, width):
        scaled_pixmap = self.pixmap.scaledToWidth(width)
        size = QSize(width, scaled_pixmap.height())
        self.setFixedSize(size)
        self.setIconSize(size)
        self.setIcon(QIcon(scaled_pixmap))

    def determineDominantColour(self):
        if self.dominant_colour is None:
            self.dominant_colour = getDominantColour(self.pixmap)
