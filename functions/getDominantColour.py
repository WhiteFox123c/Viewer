from PyQt6.QtGui import QPixmap


def getDominantColour(pixmap: QPixmap) -> int:
    res = 200
    if pixmap.width() > pixmap.height():
        if pixmap.width() > res:
            pixmap = pixmap.scaledToWidth(res)
    else:
        if pixmap.height() > res:
            pixmap = pixmap.scaledToHeight(res)

    image = pixmap.toImage()
    step = 10
    width = image.width()
    height = image.height()
    hue_dict = {}

    for x in range(0, width):
        for y in range(0, height):
            if image.pixelColor(x, y).hslSaturation() <= 10:
                continue
            hue = image.pixelColor(x, y).hslHue()
            _ = hue % step
            hue = hue - _

            if _ > step / 2:
                hue += step

            if hue_dict.get(hue) is None:
                hue_dict[hue] = 1
            else:
                hue_dict[hue] += 1
    hue_dict_keys = list(hue_dict.keys())
    if len(hue_dict_keys) == 0:
        return -1
    hue_dict_values = list(hue_dict.values())
    return hue_dict_keys[hue_dict_values.index(max(hue_dict_values))]
