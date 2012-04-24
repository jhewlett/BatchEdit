from PIL import ImageOps
import Order

class ImageBorder:
    def __init__(self, thickness):
        try:
            self.__thickness = int(thickness)
        except ValueError:
            self.__thickness = 10
            if thickness != "":
                print "Warning: could not parse --border argument '" + thickness + "'. Defaulting thickness to 10 pixels."
        
    def get_order(self):
        return Order.AFTER_RESIZE

    def process(self, image):       
        return ImageOps.expand(image, self.__thickness)
