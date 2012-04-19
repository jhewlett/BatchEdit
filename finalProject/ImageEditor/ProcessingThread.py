import threading
from PIL import Image

class ProcessingThread(threading.Thread):
    def __init__(self, file_path, output_file, commands, quality):
        self.__file_path = file_path
        self.__output_file = output_file
        self.__commands = commands
        self.__quality = quality
        
        threading.Thread.__init__(self)
    
    def run(self):
        im = Image.open(self.__file_path)
            
        for action in self.__commands:
            im = action.process(im)
        
        im.save(self.__output_file, 'JPEG', quality=self.__quality)