import sys
sys.path.append("..\\Input\\")

import BatchJob

import ImageResizer
import ImageSharpener
import pdb

from PIL import Image
from PIL.ExifTags import TAGS

import glob
import os

class BatchImageEditor:
    def __init__(self):
        pass

    def process_images(self, batch_job):
        settings = batch_job.get_settings()

        os.chdir(settings.input)

        #todo: check if input_path and output_path exist

        #todo: don't hardcode *.jpg
        for file in glob.glob("*.jpg"):
            input_file = os.path.join(settings.input, file)
            output_file = os.path.join(settings.output, file)
            
            im = Image.open(input_file)
                              
            for action in batch_job.get_commands():
                im = action.process(im)

            #don't hardcode quality?
            im.save(output_file, 'JPEG', quality = settings.quality)
