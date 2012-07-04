from PIL.ExifTags import TAGS
from PIL import Image
import Order
from Command import Command

class ImageRotater(Command):
     
    def get_order(self):
        return Order.PRE_PROCESS
    
    @classmethod
    def get_option_name(cls):
        return "--autorotate"
    
    def process(self, image):
        exif_tags = {}
        if hasattr(image, "_getexif"):
            info = image._getexif()
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif_tags[decoded] = value
            
        orientation = 1
        
        if exif_tags.has_key("Orientation"):
            orientation = exif_tags["Orientation"]

        if orientation == 1:
            pass        
        elif orientation == 2:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            image = image.rotate(180)
        elif orientation == 4:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image = image.rotate(180)
        elif orientation == 5:
            image = image.rotate(270)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 6:
            image = image.rotate(270)
        elif orientation == 7:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image = image.rotate(270)
        elif orientation == 8:
            image = image.rotate(90)

        return image