"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file name from user input
    filename = get_file()
    
    # Load image and show image before the transform
    image = SimpleImage(filename)
    image.show()

    # Apply the filter
    # TODO: your code here
    def Code_in_Place_Filter():
        for pixel in image:
            pixel.red = pixel.red * 1.5
            pixel.blue = pixel.blue * 1.5
            pixel.green = pixel.green * 0.7
        return image

    # Show the image after the transform
    Code_in_Place_Filter(image)
    image.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
