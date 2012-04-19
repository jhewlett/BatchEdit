import sys
sys.path.append("..\\ImageEditor\\")
import unittest

class Args:
    def __init__(self, args):
        self.__options = self.__parse_input(args)

    def get_options(self):
        return self.__options

    def __parse_input(self, args):
        #options = re.findall('-\w+\s?(?:".+?"|\d*\.?\d+)?', input)
        #options = re.findall('-(\w+)\s?((?:"|\').+?(?:"|\')|\d*\.?\d+)?', args)
        #options = re.findall('-(\w+)\s?(?:(?:"|\')(.+?|\d*\.?\d+)(?:"|\'))?', input)
        
        options = []
        
        for i in xrange(0, len(args)):
            if args[i].startswith("--"):
                option = args[i]
                
                if i < len(args) - 1 and not args[i+1].startswith("--"):
                    options.append((option, args[i+1]))
                else:
                    options.append((option, ""))              
                
        return options

class ArgsTests(unittest.TestCase):
    def test_parse_input(self):
        args = Args(["--saturation", "1.5", "--contrast", \
          "1.6", "--resize", "720", "--sharpen", "1.3", "--grayscale", \
          "--border", "10", "--autorotate", "--input", "c:\\input with spaces\\", \
          "--output", "c:\\output", "--quality", "85", "--forceorder", "--files", "*.jpg"])
    
        options = args.get_options()
        
        self.assertEqual([("--saturation", "1.5"), ("--contrast", "1.6"), ("--resize", "720"), \
                          ("--sharpen", "1.3"), ("--grayscale", ""), ("--border", "10"), ("--autorotate", ""), \
                          ("--input", "c:\\input with spaces\\"), ("--output", "c:\\output"), \
                          ("--quality", "85"), ("--forceorder", ""), ("--files", "*.jpg")], options)
            
if __name__ == '__main__':
    unittest.main()
