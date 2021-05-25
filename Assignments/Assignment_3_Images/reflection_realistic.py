"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    reflection = SimpleImage.blank(width, height*2) #canvas for the ori image and reflection

    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x, y)
            reflection.set_pixel(x, y, pixel)
            reflection.set_pixel(x, (height*2) - (y + 1), pixel)


    return reflection

def darker(image):
    """
    Makes image passed in darker by halving red, green, blue values.
    Note: changes in image persist after function ends.
    """
    # Demonstrate looping over all the pixels of an image,
    # changing each pixel to be half its original intensity.
    for x in range(1792):
        for y in range(1115*2):
            if y >= 1115:
                pixel = image.get_pixel(x,y)
                average = (pixel.red + pixel.green + pixel.blue) // 3
                if average >= 153:
                    pixel.red = pixel.red//2
                    pixel.green = pixel.green//2
                    pixel.blue = pixel.blue//2
                else:
                    pixel.red = average
                    pixel.blue = average
                    pixel.green = average



def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('singapore2.jpg')

    reflected = make_reflected('singapore2.jpg')

    darker(reflected)
    reflected.show()

if __name__ == '__main__':
    main()