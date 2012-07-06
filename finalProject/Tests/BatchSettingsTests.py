import unittest
import sys
import os

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(cur_dir, "..", "Input"))
sys.path.append(os.path.join(cur_dir, ".."))

from BatchSettings import BatchSettings

class BatchSettingsTests(unittest.TestCase):

    def test_parse_input_quality_less_than_1_defaults_to_95(self):
        options = [("--quality", 0)]
        settings = BatchSettings(options)
        
        self.assertEqual(95, settings.quality)
        
    def test_parse_input_quality_greater_than_100_defaults_to_95(self):
        options = [("--quality", 101)]
        settings = BatchSettings(options)
        
        self.assertEqual(95, settings.quality)
        
    def test_parse_input_quality_float_truncated(self):
        options = [("--quality", 45.5)]
        settings = BatchSettings(options)
        
        self.assertEqual(45, settings.quality)
        
    def test_parse_input_quality_does_not_parse_defaults_to_95(self):
        options = [("--quality", "blah")]
        settings = BatchSettings(options)
        
        self.assertEqual(95, settings.quality)

if __name__ == "__main__":
    unittest.main()