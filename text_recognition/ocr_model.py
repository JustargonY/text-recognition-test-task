from pathlib import Path
import easyocr
from PIL import Image


class OCRModel:
    def __init__(self):
        self.reader = easyocr.Reader(['en', 'ch_sim'], gpu=True)

    def recognize_text(self, image: Path):
        im = Image.open(image)
        result = self.reader.readtext(im.filename)
        s = ''
        for i in result:
            s += i[1] + ' '
        return s[:-1]
