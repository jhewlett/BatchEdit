class Help:
    @staticmethod
    def print_help():
        print "The following options are required:"
        print "--input [path]: A directory with images to process"
        print "--output [path]: A directory to output the process images to"
        print "-----------------------------------------------------------"
        print "The following options may be used for other settings:"
        print "--quality [value]: An integer from 1 - 100 indicating the quality of the output image. Defaults to 95."
        print "--files [filters]: String representing the file types to search for in the input directory. Defaults to '*.jpg'"
        print "--forceorder: A flag indicating whether the commands should be executed exactly in the order typed. Defaults to false."
        print "-----------------------------------------------------------"
        print "The following options are commands to perform on the images:"
        print "Many of the filters take a decimal argument for the strength. A value of 1 returns the original image."
        print "A value less than 1 will decrease the effect, while a value greater will increase it"
        print "The arguments are optional. When left out, the command will default to a subtle increase in the effect."
        print "--sharpen [strength]: Blurs or sharpens the image according to the strength."
        print "--contrast [strength]: Decreases or increases contrast based on the strength provided."
        print "--saturation [strength]: Decreases or increases the vibrance of the color."
        print "--grayscale: Converts the image to grayscale."
        print "--autorotate: Reads the exif tags of the image, if available, and attempts to auto-rotate the image accordingly."
        print "--resize [longest side]: Resizes the longest dimension in the image to the value specified. Maintains the aspect ratio. Defaults to 640 pixels."
        print "--border [thickness]: Draws a black border with the thickness specified on all sides. Defaults to 10 pixels."
        