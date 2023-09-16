from PIL import ImageEnhance
import Order
from .Command import Command

class ImageContrastEnhancer(Command):
    def __init__(self, strength):
        try:
            self.__strength = float(strength)
        except ValueError:
            self.__strength = 1.15
            if strength != "":
                print("Warning: could not parse --contrast argument '" + strength + "'. Defaulting strength to 1.15.")

    def get_order(self):
        return Order.MAIN_EDITS
    
    @classmethod
    def get_option_name(cls):
        return "--contrast"

    def process(self, image):
        contrast_enhancer = ImageEnhance.Contrast(image)
        
        return contrast_enhancer.enhance(self.__strength)
