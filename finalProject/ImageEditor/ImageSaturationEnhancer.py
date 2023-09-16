from PIL import ImageEnhance
import Order
from .Command import Command

class ImageSaturationEnhancer(Command):
    def __init__(self, strength):
        try:
            self.__strength = float(strength)
        except ValueError:
            self.__strength = 1.15
            if strength != "":
                print("Warning: could not parse --saturation argument '" + strength + "'. Defaulting strength to 1.15.")
        
    def get_order(self):
        return Order.MAIN_EDITS
    
    @classmethod
    def get_option_name(cls):
        return "--saturation"

    def process(self, image):
        saturation = ImageEnhance.Color(image)
        
        return saturation.enhance(self.__strength)
