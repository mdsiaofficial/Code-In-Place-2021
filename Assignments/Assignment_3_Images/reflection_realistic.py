"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    output = SimpleImage.blank(image.width, image.height * 2)

    for y in range(image.height):
        for x in range(image.width):
            px = image.get_pixel(x, y)
            # Upper side
            output.set_pixel(x, y, px)
            # Reflected pixel from the original image
            rx = x + (y * 0.1) * math.sin(5000 / (y + 1))
            ry = image.height - y - 1 + (y * 0.03) * math.sin(x / 30)
            if rx < 0:
                rx = 0
            if rx > image.width - 1:
                rx = image.width - 1
            if ry < 0:
                ry = 0;
            if ry > image.height - 1:
                ry = image.height - 1
            rpx = image.get_pixel(rx, ry)
            # Color correction
            opx = output.get_pixel(x, image.height + y)
            opx.red = 20 + rpx.red * 0.1
            opx.green = 20 + rpx.green * 0.3
            opx.blue = 20 + rpx.blue * 0.4

    return output


def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()