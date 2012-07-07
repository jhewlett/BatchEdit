import unittest
import sys
import os

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(cur_dir, "..", "Input"))
sys.path.append(os.path.join(cur_dir, ".."))

from ImageEditor import ImageBorder

class ImageBorderTests(unittest.TestCase):
    
    def test_init(self):
        border = ImageBorder.ImageBorder("10,red")
                
        self.assertEqual(10, border.thickness)
        self.assertEqual("red", border.color)
    
    def test_init_no_color_given_defaults_to_black(self):
        border = ImageBorder.ImageBorder("10")
        
        self.assertEqual("black", border.color)
        self.assertEqual(10, border.thickness)
        
    def test_init_cannot_parse_thickness_defaults_to_10(self):
        border = ImageBorder.ImageBorder("str")
                
        self.assertEqual(10, border.thickness)
        self.assertEqual("black", border.color)