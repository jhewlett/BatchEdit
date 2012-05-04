from ImageEditor import ImageBorder
from ImageEditor import ImageResizer
from ImageEditor import ImageContrastEnhancer
from ImageEditor import ImageSaturationEnhancer
from ImageEditor import ImageSharpener
from ImageEditor import ImageRotater
from ImageEditor import ImageWatermark
from ImageEditor import ImageBrightnessEnhancer
import BatchSettings

class BatchJob:
    def __init__(self, tokens):
        self.__commands, self.__settings = self.__parse_tokens(tokens)

    def __parse_tokens(self, tokens):     
        settings = BatchSettings.BatchSettings(tokens)
        commands = []
        for token1, token2 in tokens:
            command = None
            
            if token1 == "--sharpen":
                command = ImageSharpener.ImageSharpener(token2)
            elif token1 == "--resize":
                command = ImageResizer.ImageResizer(token2)
            elif token1 == "--contrast":
                command = ImageContrastEnhancer.ImageContrastEnhancer(token2)
            elif token1 == "--saturation":
                command = ImageSaturationEnhancer.ImageSaturationEnhancer(token2)
            elif token1 == "--grayscale":
                command = ImageSaturationEnhancer.ImageSaturationEnhancer(0)
            elif token1 == "--border":
                if "," in token2:
                    args = token2.split(",")
                else:
                    args = [token2, "black"]
                command = ImageBorder.ImageBorder(args[0], args[1])
            elif token1 == "--autorotate":
                command = ImageRotater.ImageRotater()
            elif token1 == "--watermark":
                command = ImageWatermark.ImageWatermark(token2)
            elif token1 == "--brightness":
                command = ImageBrightnessEnhancer.ImageBrightnessEnhancer(token2)
            
            if command != None:
                commands.append(command)
                
        if not settings.force_order:
            commands = self.__order_commands(commands)

        return (commands, settings)
    
    def __order_commands(self, commands):
        return sorted(commands, key = lambda command : command.get_order())

    def get_commands(self):
        return self.__commands

    def get_settings(self):
        return self.__settings
