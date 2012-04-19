from PIL import ImageEnhance

class ImageSaturationEnhancer:
    def __init__(self, strength):
        self.__strength = strength

    def process(self, image):
        saturation = ImageEnhance.Color(image)
        
        return saturation.enhance(self.__strength)
