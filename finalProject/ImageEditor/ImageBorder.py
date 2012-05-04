from PIL import ImageOps
import Order

class ImageBorder:
    def __init__(self, thickness, color):
        try:
            self.__thickness = int(thickness)
        except ValueError:
            self.__thickness = 10
            if thickness != "":
                print "Warning: could not parse --border thickness argument '" + thickness + "'. Defaulting thickness to 10 pixels."
                
        self.__color = color      
        
    def get_order(self):
        return Order.AFTER_RESIZE

    def process(self, image):     
        try:
            return ImageOps.expand(image, self.__thickness, fill=self.__color)
        except ValueError:
            print "Warning: could not parse --border color argument '" + self.__color + "'. Defaulting color to black."
            return ImageOps.expand(image, self.__thickness, fill="black")
