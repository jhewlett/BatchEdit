from ImageEditor import ImageSaturationEnhancer

class ImageGrayscaleConverter(ImageSaturationEnhancer.ImageSaturationEnhancer):
    
    def __init__(self, token):
        super(ImageGrayscaleConverter, self).__init__(0)
        
    @classmethod
    def get_option_name(cls):
        return "--grayscale"