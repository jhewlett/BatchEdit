class Command(object):
    def __init__(self, args):
        pass
    
    def get_order(self):
        pass
    
    def process(self, image):
        pass
    
    @classmethod
    def get_option_name(cls):
        pass
    
    @classmethod
    def parse(cls, options, commands):
        for option in options[:]:
            name, value = option
            if name == cls.get_option_name():
                commands.append(cls(value))
                options.remove(option)
                