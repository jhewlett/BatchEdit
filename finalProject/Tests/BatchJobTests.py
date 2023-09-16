import os
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(cur_dir, "..", "Input"))
sys.path.append(os.path.join(cur_dir, ".."))

import BatchJob
import unittest

class BatchJobTests(unittest.TestCase):
    def test_parse_input_settings(self):
        options = [("--input", "c:\\input with spaces\\"), ("--output", "c:\\output\\"), \
                      ("--quality", "85"), ("--forceorder", ""), ("--files", "*.jpg"), ("--help", "")]
        job = BatchJob.BatchJob(options)
        settings = job.get_settings()
        
        self.assertEqual(True, settings.force_order)
        self.assertEqual(85, settings.quality)
        self.assertEqual('c:\\input with spaces\\', settings.input)
        self.assertEqual('c:\\output\\', settings.output)
        self.assertEqual('*.jpg', settings.files)
        self.assertEqual(False, settings.process)
        self.assertEqual(True, settings.show_help)
        
        self.assertEqual(0, len(options), "Did not remove options along the way.")
#        
    def test_parse_input_commands(self):
        options = [("--saturation", "1.5"), ("--contrast", "1.6"), ("--resize", "720"), ("--sharpen", "1.3"), \
                        ("--grayscale", ""), ("--border", "10"), ("--autorotate", ""), ("--watermark", "C:\test.png")]
        
        job = BatchJob.BatchJob(options)
        commands = job.get_commands()
        
        self.assertEqual(8, len(commands))
        
        for i in range(0, len(commands) - 1):
            self.assertTrue(commands[i].get_order() <= commands[i+1].get_order(), "Did not order the commands")
                    
        self.assertEqual(0, len(options), "Did not remove options along the way.")
           
if __name__ == '__main__':
    unittest.main()