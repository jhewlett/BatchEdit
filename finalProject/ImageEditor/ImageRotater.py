from PIL.ExifTags import TAGS
from PIL import Image

class ImageRotater:
    
    def __init__(self):
        pass
    
    def process(self, image):
        ret = {}
        info = image._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
            
        orientation = 1
        try:
            orientation = ret["Orientation"]
        except KeyError:
            return image
        
        if orientation == 2:
            return image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            return image.rotate(180)
        elif orientation == 4:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            return image.rotate(180)
        elif orientation == 5:
            image = image.rotate(270)
            return image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 6:
            return image.rotate(270)
        elif orientation == 7:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            return image.rotate(270)
        elif orientation == 8:
            return image.rotate(90)
        else:
            return image