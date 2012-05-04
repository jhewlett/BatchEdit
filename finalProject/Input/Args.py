class Args:
    def __init__(self, args):
        self.__options = self.__parse_input(args)

    def get_options(self):
        return self.__options

    def __parse_input(self, args):
        options = []
        
        for i in xrange(0, len(args)):
            if args[i].startswith("--"):
                option = args[i]
                
                if i < len(args) - 1 and not args[i+1].startswith("--"):
                    options.append((option, args[i+1]))
                else:
                    options.append((option, ""))              
                
        return options
