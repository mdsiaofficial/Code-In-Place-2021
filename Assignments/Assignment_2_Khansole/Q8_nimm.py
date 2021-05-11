"""
The game of Nimm goes as follows:

The game starts with a pile of 20 stones between the players.

The two players alternate turns.

On a given turn, a player may take either 1 or 2 stone from the center pile.

The two players continue until the center pile has run out of stones.
"""

def main():

    stones=20   # stones that appears before starting game
    player=1    # dummy player count, it will increase and decrease

    while stones>0:
        # this outputs as asked in the description
        print("There are",stones,"stones left")
        removed_stones=int(input("Player " +str(player)+" would you like to remove 1 or 2 stones? "))

        # this loop for checking user inputs other than 1 or 2
        while removed_stones!=1 and removed_stones!=2:
            removed_stones = 0
            removed_stones=int(input("Please enter 1 or 2: "))
        print("")

        stones-=removed_stones
        if player ==1:
            player+=1
        else:
            player-=1
    print("Player "+str(player)+" wins!")

if __name__ == '__main__':
    main()
