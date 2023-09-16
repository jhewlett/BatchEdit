from PIL import Image
import Order
import os
from .Command import Command

class ImageWatermark(Command):
    def __init__(self, path_to_watermark):
        
        self.__path = path_to_watermark
        
        if "~" in self.__path:
            self.__path = os.path.expanduser(self.__path)

        if os.path.exists(self.__path):
            self.__path = os.path.abspath(self.__path)
        
    def get_order(self):
        return Order.AFTER_RESIZE
    
    @classmethod
    def get_option_name(cls):
        return "--watermark"

    def process(self, image):
        if os.path.isfile(self.__path):
            try:
                mark = Image.open(self.__path)
            except IOError:
                print("Warning: could not open watermark file '" + self.__path + "'. Ensure that it is a valid image file.")
                return image
            
            width = mark.size[0]
            height = mark.size[1]
            
            mid = int(image.size[0] / 2)
            left_point = int(mid - width / 2)
            right_point = left_point + width
            
            if mark.mode == "RGBA":
                mask = mark
            else:
                mask = None
            
            image.paste(mark, (left_point, image.size[1] - height - 30, right_point, image.size[1] - 30), mask)
            
            return image
        else:
            print("Warning: could not find watermark file '" + self.__path + "'.")
            return image