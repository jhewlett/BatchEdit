from PIL import ImageOps
import Order
from Command import Command

class ImageBorder(Command):
    def __init__(self, args):
        
        if ',' in args:
            parts = args.split(',')
            thickness = parts[0]
            self.__color = parts[1]
        else:
            thickness = args
            self.__color = "black"
                
        try:
            self.__thickness = int(thickness)
        except ValueError:
            self.__thickness = 10
            if thickness != "":
                print "Warning: could not parse --border thickness argument '" + thickness + "'. Defaulting thickness to 10 pixels."    
        
    def get_order(self):
        return Order.AFTER_RESIZE
    
    @classmethod
    def get_option_name(cls):
        return "--border"

    def process(self, image):     
        try:
            return ImageOps.expand(image, self.__thickness, fill=self.__color)
        except ValueError:
            print "Warning: could not parse --border color argument '" + self.__color + "'. Defaulting color to black."
            return ImageOps.expand(image, self.__thickness, fill="black")
