import os
import Help

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
        for token1, token2 in tokens:     
            if token1 == "--help":
                Help.Help.print_help()
                self.process = False
                self.show_help = True
                break   
            if token1 == "--quality":
                try:
                    self.quality = int(token2)
                except ValueError:
                    print "Warning: could not parse --quality argument '" + token2 + "'. Defaulting quality to 95."
                else:
                    if self.quality < 1 or self.quality > 100:
                        print "Warning: --quality argument needs to be between 1 and 100. Defaulting quality to 95."
                        self.quality = 95
            elif token1 == "--input":
                self.input = self.__check_expand_user(token2)
            elif token1 == "--output":
                self.output = self.__check_expand_user(token2)
            elif token1 == "--files":
                self.files = token2
            elif token1 == "--forceorder":
                self.force_order = True
                
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
    
    #Needed for Linux, where ~ represents the current user directory
    def __check_expand_user(self, path):
        if "~" in path:
            path = os.path.expanduser(path)
        return path
    
    def __check_dir_exists(self, path, path_name):
        if not os.path.isdir(path):
            if not self.show_help:
                print "Error: could not find " + path_name + " directory '" + path + "'."
            return False
        return True 
    
