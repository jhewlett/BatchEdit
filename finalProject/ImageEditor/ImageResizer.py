from PIL import Image
import Order

class ImageResizer:
    def __init__(self, longest_dim):
        
        try:
            self.__dim = int(longest_dim)        
        except ValueError:
            self.__dim = 640
            if longest_dim != "":
                print "Warning: could not parse --resize argument '" + longest_dim + "'. Defaulting size to 640."
        
    def get_order(self):
        return Order.AFTER_MAIN_EDITS 

    def process(self, image):
        image.thumbnail((self.__dim, self.__dim), Image.ANTIALIAS)

        return image
