"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage_warhole import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    patch1 = make_recolored_patch(1.5, 0, 1.5)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pixel = patch1.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            # final_image.set_pixel((WIDTH/3)+(x+1), y, pixel)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here
    for p in patch:
        p.red *= red_scale
        p.green *= green_scale
        p.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()