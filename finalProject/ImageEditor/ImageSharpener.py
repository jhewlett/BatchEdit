from PIL import ImageEnhance

class ImageSharpener:
    def __init__(self, strength):
        self.__strength = strength

    def process(self, image):
        sharpener = ImageEnhance.Sharpness(image)
        
        return sharpener.enhance(self.__strength)
