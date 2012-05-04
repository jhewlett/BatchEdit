from PIL import Image
import Order

class ImageResizer:
    def __init__(self, final_size):
        
        try:
            self.__new_longest_dim = int(final_size)
        except ValueError:
            self.__new_longest_dim = 640
            if final_size != "":
                print "Warning: could not parse --resize argument '" + final_size + "'. Defaulting longest dimension to 640 px."
        
    def get_order(self):
        return Order.AFTER_MAIN_EDITS

    def process(self, image):  
        new_width, new_height = self.__get_new_size(image.size, self.__new_longest_dim)
                    
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
            
        return image
    
    def __get_new_size(self, size, new_max_dim):
        
        orig_width = size[0]
        orig_height = size[1]
        
        if orig_width > orig_height:
            new_width = new_max_dim

            ratio = orig_width / float(orig_height)

            new_height = int(new_width / ratio)
        else:
            new_height = new_max_dim

            ratio = orig_height / float(orig_width)

            new_width = int(new_height / ratio)
            
        return (new_width, new_height)
