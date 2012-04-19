class BatchSettings:
    def __init__(self, tokens):
        self.input = ""
        self.output = ""
        self.quality = 95
        self.files = "*.jpg"
        self.force_order = False
        
        self.__parse_input(tokens)

    def __parse_input(self, tokens):
        for token1, token2 in tokens:        
            if token1 == "--quality":
                try:
                    self.quality = int(token2)
                except ValueError:
                    print "Warning: could not parse --quality argument '" + token2 + "'. Defaulting quality to 95."
            elif token1 == "--input":
                self.input = token2
            elif token1 == "--output":
                self.output = token2
            elif token1 == "--files":
                self.files = token2
            elif token1 == "--forceorder":
                self.force_order = True
    
