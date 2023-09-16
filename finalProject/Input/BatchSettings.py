import os
from Help import Help

class BatchSettings:
    def __init__(self, options):
        self.input = ""
        self.output = ""
        self.quality = 95
        self.files = "*.jpg"
        self.force_order = False
        self.process = True
        self.show_help = False
        
        self.__parse_input(options)

    def __parse_input(self, options):
        for option in options[:]:
            name, value = option
            
            match = True
              
            if name == "--help":
                self.process = False
                self.show_help = True 
            elif name == "--quality":
                try:
                    self.quality = int(value)
                except ValueError:
                    print("Warning: could not parse --quality argument '" + value + "'. Defaulting quality to 95.")
                else:
                    if self.quality < 1 or self.quality > 100:
                        print("Warning: --quality argument needs to be between 1 and 100. Defaulting quality to 95.")
                        self.quality = 95
                        
            elif name == "--input":
                self.input = value
            elif name == "--output":
                self.output = value
            elif name == "--files":
                self.files = value
            elif name == "--forceorder":
                self.force_order = True
            else:
                match = False
                
            if match:
                options.remove(option)
            
    def check_paths(self):
        self.input = self.__check_expand_user(self.input)
        self.output = self.__check_expand_user(self.output)
        
        if self.__check_dir_exists(self.input):
            self.input = os.path.abspath(self.input)
        else:
            self.process = False
            return
            
        if not os.path.isdir(self.output):
            try:
                self.output = os.path.abspath(self.output)
                os.makedirs(self.output)
            except OSError:
                print("Error: output path '" + self.output + "' does not exist and could not be created.")
                self.process = False
        else:
            self.output = os.path.abspath(self.output)
    
    def __check_expand_user(self, path):
        """Needed for Linux, where ~ represents the current user directory"""
        if "~" in path:
            path = os.path.expanduser(path)
        return path
    
    def __check_dir_exists(self, path):
        if not os.path.isdir(path):
            print("Error: could not find input directory '" + path + "'.")
            return False
        return True 
    
