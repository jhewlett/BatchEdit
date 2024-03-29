from PIL import ImageEnhance
import Order
from .Command import Command

class ImageSharpener(Command):
    def __init__(self, strength):
        
        try:
            self.__strength = float(strength)
        except ValueError:
            self.__strength = 1.3
            if strength != "":
                print("Warning: could not parse --sharpen argument '" + strength + "'. Defaulting strength to 1.3.")
        
    def get_order(self):
        return Order.AFTER_RESIZE
    
    @classmethod
    def get_option_name(cls):
        return "--sharpen"

    def process(self, image):
        sharpener = ImageEnhance.Sharpness(image)
        
        return sharpener.enhance(self.__strength)
            
