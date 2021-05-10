"""
The game of Nimm goes as follows:

The game starts with a pile of 20 stones between the players.

The two players alternate turns.

On a given turn, a player may take either 1 or 2 stone from the center pile.

The two players continue until the center pile has run out of stones.
"""

import random

def main():
    stones=20
    player=1
    while stones>0:
        print("There are ",stones,"stones left")
        removed_stones=int(input("Player " +str(player)+" would you like to remove 1 or 2 stones? "))
        print("")
        while removed_stones!=1 and removed_stones!=2:
            print("Please enter between 1 or 2: ")
        stones-=removed_stones
        if player ==1:
            player+=1
        else:
            player-=1


    print("Player "+str(player)+" wins!")

if __name__ == '__main__':
    main()
