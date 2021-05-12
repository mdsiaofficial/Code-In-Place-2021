from karel.stanfordkarel import *

def main():

    while front_is_clear():
        make_wave()
        go_to_next_step()

def go_to_next_step():
    turn_right()
    move()
    move()
    turn_right()
    move()
    turn_left()


def make_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()


# There is no need to edit code beyond this point
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program('Karel_Makes_Waves.w')
