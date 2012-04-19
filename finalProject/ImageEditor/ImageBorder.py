from PIL import ImageOps

class ImageBorder:
    def __init__(self, thickness):
        self.__thickness= thickness

    def process(self, image):       
        return ImageOps.expand(image, self.__thickness)
