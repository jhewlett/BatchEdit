import os
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(cur_dir, "..", "Input"))

import Args
import unittest

class ArgsTests(unittest.TestCase):
    def test_parse_input(self):
        args = Args.Args(["--saturation", "1.5", "--contrast", \
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