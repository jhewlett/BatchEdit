from ImageEditor import *
from BatchSettings import BatchSettings

class BatchJob:
    def __init__(self, tokens):
        self.__commands, self.__settings = self.__parse_tokens(tokens)

    def __parse_tokens(self, tokens):     
        settings = BatchSettings(tokens)

        commands = []
        
        for commandSub in self.__get_all_commands(Command.Command):
            commandSub.parse(tokens, commands)
                
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
