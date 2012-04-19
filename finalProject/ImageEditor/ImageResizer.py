from PIL import Image

class ImageResizer:
    def __init__(self, longest_dim):
        self.__dim = longest_dim

    def process(self, image):
        image.thumbnail((self.__dim, self.__dim), Image.ANTIALIAS)

        return image
