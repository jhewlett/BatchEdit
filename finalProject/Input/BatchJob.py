import sys
sys.path.append("..\\ImageEditor\\")
from ImageEditor import ImageBorder
from ImageEditor import ImageResizer
from ImageEditor import ImageContrastEnhancer
from ImageEditor import ImageSaturationEnhancer
from ImageEditor import ImageSharpener
from ImageEditor import ImageRotater
import BatchSettings
import unittest

class BatchJob:
    def __init__(self, tokens):
        self.__commands, self.__settings = self.__parse_tokens(tokens)

    def __parse_tokens(self, tokens):     
        settings = BatchSettings.BatchSettings(tokens)
        commands = []
        for token1, token2 in tokens:
            command = None
            
            if token1 == "--sharpen":
                try:
                    command = ImageSharpener.ImageSharpener(float(token2))
                except ValueError:
                    if token2 != "":
                        print "Warning: could not parse --sharpen argument '" + token2 + "'. Defaulting strength to 1.3."
                    command = ImageSharpener.ImageSharpener(1.3)
            elif token1 == "--resize":
                try:
                    command = ImageResizer.ImageResizer(int(token2))
                except ValueError:
                    if token2 != "":
                        print "Warning: could not parse --resize argument '" + token2 + "'. Defaulting size to 640."
                    command = ImageResizer.ImageResizer(640)
            elif token1 == "--contrast":
                try:
                    command = ImageContrastEnhancer.ImageContrastEnhancer(float(token2))
                except ValueError:
                    if token2 != "":
                        print "Warning: could not parse --contrast argument '" + token2 + "'. Defaulting strength to 1.25."
                    command = ImageContrastEnhancer.ImageContrastEnhancer(1.25)
            elif token1 == "--saturation":
                try:
                    command = ImageSaturationEnhancer.ImageSaturationEnhancer(float(token2))
                except ValueError:
                    if token2 != "":
                        print "Warning: could not parse --saturation argument '" + token2 + "'. Defaulting strength to 1.15."
                        command = ImageSaturationEnhancer.ImageSaturationEnhancer(1.15)
            elif token1 == "--grayscale":
                command = ImageSaturationEnhancer.ImageSaturationEnhancer(0)
            elif token1 == "--border":
                try:
                    command = ImageBorder.ImageBorder(int(token2))
                except ValueError:
                    if token2 != "":
                        print "Warning: could not parse --border argument '" + token2 + "'. Defaulting thickness to 10 pixels."
                        
                    command = ImageBorder.ImageBorder(10)
            elif token1 == "--autorotate":
                command = ImageRotater.ImageRotater()

            if command != None:
                commands.append(command)

        return (commands, settings)

    def get_commands(self):
        return self.__commands

    def get_settings(self):
        return self.__settings
    
class BatchJobTests(unittest.TestCase):
    def test_parse_input_settings(self):
        options = [("--input", "c:\\input with spaces\\"), ("--output", "c:\\output"), \
                      ("--quality", "85"), ("--forceorder", ""), ("--files", "*.jpg")]
        job = BatchJob(options)
        settings = job.get_settings()
        
        self.assertEqual(True, settings.force_order)
        self.assertEqual(85, settings.quality)
        self.assertEqual('c:\\input with spaces\\', settings.input)
        self.assertEqual('c:\\output', settings.output)
        self.assertEqual('*.jpg', settings.files)
        
    def test_parse_input_commands(self):
        options = [("--saturation", "1.5"), ("--contrast", "1.6"), ("--resize", "720"), \
                      ("--sharpen", "1.3"), ("--grayscale", ""), ("--border", "10"), ("--autorotate", "")]
        
        job = BatchJob(options)
        commands = job.get_commands()
        
        self.assertEqual(7, len(commands))
            
if __name__ == '__main__':
    unittest.main()
