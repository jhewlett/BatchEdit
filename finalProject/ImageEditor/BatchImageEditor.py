import sys
sys.path.append("..\\Input\\")

import BatchJob
import ImageResizer
import ImageSharpener
import ProcessingThread

from PIL import Image
from PIL.ExifTags import TAGS

import glob
import os

class BatchImageEditor:
    def __init__(self):
        pass

    def process_images(self, batch_job):
        settings = batch_job.get_settings()

        if not os.path.isdir(settings.input):
            print "Error: could not find input directory '" + settings.input + "'"
            return

        if not os.path.isdir(settings.output):
            print "Error: could not find output directory '" + settings.output + "'"
            return
        
        self.__process_input_images(batch_job, settings)
        
    def __process_input_images(self, batch_job, settings):
        os.chdir(settings.input)
        
        print "Getting images from '" + settings.input + "'"
        
        count = 0
        
        threads = []
        
        for file_name in glob.glob(settings.files):
            count += 1
            
            input_file = os.path.join(settings.input, file_name)
            output_file = os.path.join(settings.output, file_name)
            
            print "Processing image '" + file_name + "'"
            
           # thread = ProcessingThread.ProcessingThread(input_file, output_file, batch_job.get_commands(), settings.quality)
            #threads.append(thread)
            
           # thread.start()
            
            im = Image.open(input_file)
            
            for action in batch_job.get_commands():
                im = action.process(im)
            
            im.save(output_file, 'JPEG', quality=settings.quality)
            
        for t in threads:
            t.join()
            
        if count == 0:
            print "Could not find any files matching filter '" + settings.files + "'"
        else:
            print "Finished processing " + str(count) + " files to '" + settings.output + "'"
