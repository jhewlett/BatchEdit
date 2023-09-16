from ImageEditor import *
from BatchSettings import BatchSettings

class BatchJob:
    def __init__(self, options):
        self.__commands, self.__settings = self.__parse_tokens(options)

    def __parse_tokens(self, options):     
        settings = BatchSettings(options)

        commands = []
        
        for commandSub in self.__get_all_commands(Command.Command):
            commandSub.parse(options, commands)
            
        for name, value in options:
            print("Warning: option '" + name + "' is not recognized." )
                
        if not settings.force_order:
            commands = self.__order_commands(commands)

        return (commands, settings)
    
    def __get_all_commands(self, cls):
        """Recursively get all subclasses of cls"""
        sub_classes = []
        for sub in cls.__subclasses__():
            sub_classes.append(sub)
            sub_classes.extend(self.__get_all_commands(sub))
        return sub_classes     
            
    def __order_commands(self, commands):
        return sorted(commands, key = lambda command : command.get_order())

    def get_commands(self):
        return self.__commands

    def get_settings(self):
        return self.__settings
