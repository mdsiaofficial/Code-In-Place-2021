from karel.stanfordkarel import *

def main():

    


# There is no need to edit code beyond this point
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program('Karel_Makes_Waves.w')
