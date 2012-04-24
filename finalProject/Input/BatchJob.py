import sys
sys.path.append("..\\ImageEditor\\")
from ImageEditor import ImageBorder
from ImageEditor import ImageResizer
from ImageEditor import ImageContrastEnhancer
from ImageEditor import ImageSaturationEnhancer
from ImageEditor import ImageSharpener
from ImageEditor import ImageRotater
import BatchSettings
import Help
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
                command = ImageBorder.ImageBorder(token2)
            elif token1 == "--autorotate":
                command = ImageRotater.ImageRotater()
            elif token1 == "--help":
                Help.Help.print_help()
                #signal that we don't want to process the images
                settings.process = False
                break
            
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
        # Make sure it got sorted
        for i in xrange(0, len(commands) - 1):
            self.assertTrue(commands[i].get_order() <= commands[i+1].get_order())
            
if __name__ == '__main__':
    unittest.main()
