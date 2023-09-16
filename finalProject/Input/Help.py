class Help:
    @staticmethod
    def print_help():
        print("Required Settings:")
        print("--input [path]: A directory with images to process.")
        print("--output [path]: A directory to output the process images to. The directory must exist.")
        print("-----------------------------------------------------------")
        print("Optional Settings:")
        print("--quality [value]: An integer from 1 - 100 indicating the quality of the output image. Defaults to 95.")
        print("--files [filters]: String representing the file types to search for in the input directory. Defaults to '*.jpg'.")
        print("--forceorder: A flag indicating whether the commands should be executed exactly in the order typed. Defaults to false.")
        print("-----------------------------------------------------------")
        print("Photo Operations:")
        print("--sharpen [strength]: Blurs or sharpens the image according to the strength.")
        print("--contrast [strength]: Decreases or increases contrast based on the strength provided.")
        print("--brightness [strength]: Decreases or increases brightness based on the strength provided.")
        print("--saturation [strength]: Decreases or increases the vibrancy of the color.")
        print("--grayscale: Converts the image to grayscale.")
        print("--autorotate: Reads the exif tags of the image, if available, and attempts to auto-rotate the image accordingly.")
        print("--resize [longest side]: Resizes the longest dimension in the image to the value specified. Maintains the aspect ratio. Defaults to 640 pixels.")
        print("--border [thickness[,color]]: Draws a black border with the thickness and color specified on all sides. Defaults to 10 pixels with a fill of black.")
        print("--watermark [path to image]: Overlays the specified image in the lower middle as a watermark. Supports transparency.")
        