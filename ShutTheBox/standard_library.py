# standard_library.py
"""Python Essentials: The Standard Library.
Alex Mannewitz
Math 345 - 001
Sept 12, 2024
"""

import itertools as it
import box as box
import time
import sys
import random


def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""

    # Set initial values
    won = False
    start_time = time.time()
    end_time = start_time + timelimit
    numbers_remaining = list(range(1,10))

    # Repeat the game sequence until a win or loss
    while True:
        
        print()    # New line for appearance

        # Check if numbers is empty or if time is out. If it is, break the loop to print game over sequence
        if len(numbers_remaining) == 0:
            won = True
            break

        if time.time() >= end_time:
            print("Times up!")
            break

        # Roll 1 dice if the max number is 6 or less, roll 2 dice if the max number is more than 6
        if max(numbers_remaining) <= 6:
            roll = random.randint(1,6)
        else:
            roll = random.randint(1,6) + random.randint(1,6)


        # Print out the players turn and accept their choice of numbers to eliminate
        if box.isvalid(roll, numbers_remaining):
            print (f"Numbers remaining: {numbers_remaining}")
            print (f"Roll: {roll}")

            # Checks if the input of numbers to eliminate is valid
            while True:
                print (f"Seconds left: {round((end_time - time.time()), 1)}")
                eliminate_string = input("Numbers to eliminate: ")
                eliminate_list = box.parse_input(eliminate_string, numbers_remaining)
                if sum(eliminate_list) == roll:
                    break
                else:
                    print("Invalid input\n")

                    # Test time again 
                    if time.time() >= end_time:
                        break


            for i in eliminate_list:
                numbers_remaining.remove(i)
    
        # If the roll is invalid, break the loop to print game over sequence.
        else: 
            break


    # Print end game sequence
    if numbers_remaining:   # if numbers_remaining still has numbers
        print("Game over!")
    print()
    print(f"Score for player {player}: {sum(numbers_remaining)} points")
    print(f"Time played: {round(time.time() - start_time, 1)} seconds")

    if won:   # if they won the game
        print("Congratulations!! You shut the box!")
    else:
        print("Better luck next time :)")
    

if __name__ == "__main__":
    if len(sys.argv) == 3:
        shut_the_box(sys.argv[1], float(sys.argv[2]))