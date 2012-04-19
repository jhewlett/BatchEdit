from PIL import ImageEnhance

class ImageContrastEnhancer:
    def __init__(self, strength):
        self.__strength = strength

    def process(self, image):
        contrast_enhancer = ImageEnhance.Contrast(image)
        
        return contrast_enhancer.enhance(self.__strength)
