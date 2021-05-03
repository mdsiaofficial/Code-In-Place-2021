from karel.stanfordkarel import *


def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()

def build_hospital():
    turn_left()
    build_column()
    turn_right()
    move()
    turn_right()
    build_column()
    turn_left()

def build_column():
    if beepers_present():
        move()
    else:
        put_beeper()
        move()
    #two beepers left to place
    put_beeper()
    move()
    put_beeper()

def turn_right():
    for _ in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program('Hospital.w')