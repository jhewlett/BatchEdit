from PIL import ImageEnhance
import Order

class ImageBrightnessEnhancer:
    def __init__(self, strength):
        try:
            self.__strength = float(strength)
        except ValueError:
            self.__strength = 1
            if strength != "":
                print "Warning: could not parse --brightness argument '" + strength + "'. Defaulting strength to 1."

    def get_order(self):
        return Order.MAIN_EDITS

    def process(self, image):
        brightness_enhancer = ImageEnhance.Brightness(image)
        
        return brightness_enhancer.enhance(self.__strength)
