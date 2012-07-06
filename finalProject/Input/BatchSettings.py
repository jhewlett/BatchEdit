import os
from Help import Help

class BatchSettings:
    def __init__(self, tokens):
        self.input = ""
        self.output = ""
        self.quality = 95
        self.files = "*.jpg"
        self.force_order = False
        self.process = True
        self.show_help = False
        
        self.__parse_input(tokens)

    def __parse_input(self, tokens):
        for token in tokens[:]:
            name, value = token
            
            match = True
              
            if name == "--help":
                Help.print_help()
                self.process = False
                self.show_help = True
                break   
            
            if name == "--quality":
                try:
                    self.quality = int(value)
                except ValueError:
                    print "Warning: could not parse --quality argument '" + value + "'. Defaulting quality to 95."
                else:
                    if self.quality < 1 or self.quality > 100:
                        print "Warning: --quality argument needs to be between 1 and 100. Defaulting quality to 95."
                        self.quality = 95
                        
            elif name == "--input":
                self.input = self.__check_expand_user(value)
            elif name == "--output":
                self.output = self.__check_expand_user(value)
            elif name == "--files":
                self.files = value
            elif name == "--forceorder":
                self.force_order = True
            else:
                match = False
                
            if match:
                tokens.remove(token)
                
        if self.__check_dir_exists(self.input, "input"):
            self.input = os.path.abspath(self.input)
        else:
            self.process = False
            
        if not os.path.isdir(self.output):
            try:
                self.output = os.path.abspath(self.output)
                os.makedirs(self.output)
            except OSError:
                print "Error: output path '" + self.output + "' does not exist and could not be created."
                self.process = False
        else:
            self.output = os.path.abspath(self.output)
    
    def __check_expand_user(self, path):
        """Needed for Linux, where ~ represents the current user directory"""
        if "~" in path:
            path = os.path.expanduser(path)
        return path
    
    def __check_dir_exists(self, path, path_name):
        if not os.path.isdir(path):
            if not self.show_help:
                print "Error: could not find " + path_name + " directory '" + path + "'."
            return False
        return True 
    
