from PIL import ImageEnhance
import Order

class ImageContrastEnhancer:
    def __init__(self, strength):
        try:
            self.__strength = float(strength)
        except ValueError:
            self.__strength = 1.15
            if strength != "":
                print "Warning: could not parse --contrast argument '" + strength + "'. Defaulting strength to 1.15."

    def get_order(self):
        return Order.MAIN_EDITS

    def process(self, image):
        contrast_enhancer = ImageEnhance.Contrast(image)
        
        return contrast_enhancer.enhance(self.__strength)
