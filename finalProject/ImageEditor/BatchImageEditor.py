from PIL import Image
from PIL.ExifTags import TAGS
from Input import Help

import glob
import os

class BatchImageEditor:
    def __init__(self):
        pass

    def process_images(self, batch_job):
        settings = batch_job.get_settings()
        
        if settings.show_help:
            Help.Help.print_help()
        else:
            settings.check_paths()        
        
        if settings.process:
            os.chdir(settings.input)
            
            print "Getting images from '" + settings.input + "'."
            
            count = 0
  
            for file_name in glob.glob(settings.files):
                input_file = os.path.join(settings.input, file_name)
                output_file = os.path.join(settings.output, file_name)
                
                try:
                    im = Image.open(input_file)
                except IOError:
                    print "Warning: could not open input file '" + file_name + "'. Ensure that it is a valid image."
                    continue
                
                print "Processing image '" + file_name + "'."
                
                count += 1
                
                for command in batch_job.get_commands():
                    im = command.process(im)
                
                im.save(output_file, 'JPEG', quality=settings.quality)
                
                del im
                
            if count == 0:
                print "Could not find any image files matching filter '" + settings.files + "'."
            else:
                print "Finished processing " + str(count) + " file(s) to '" + settings.output + "'."
