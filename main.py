#                                                                NUMBER GUESSING GAME

import random
import time
play_again = True
while play_again is True:
    num1 = int(input("Enter a number between 1 and anything.\n"))
    number = random.randint(1,num1)
    end_of_game = False
    lives= int(input(("How many guesses do you give yourself?\n")))
    print(f"Guess a number between 1 and {num1}. You have {lives} guesses.\n")
    while not end_of_game:
        time.sleep(2)
        guess = int(input("Guess a number: "))
        if guess > number:
            print("Too high.")
            lives -= 1
            (print(f"You have {lives} guesses left\n"))
        elif guess < number:
            print("Too low.")
            lives -= 1
            (print(f"You have {lives} guesses left\n"))
        else:
            print(f"Good guessing! {number} is correct!")
            print(f"             NOOOOOICE DUDE! YOU REKT THE COMPUTER!\n")
            break
        if lives == 0:
            end_of_game = True
            print(f"             WAAAAAAMP! GAME OVER! The mystery number was {number}.\n")
    play_again = input("Would you like to play again? 'yes' or 'no': ").lower()
    if play_again == "no":
        play_again = False
        print("                   SEEEEEEEE YAAAAAAAAAA!")
        end_of_game = True
    else:
        play_again = True
        print("          HAPPY NUMBER HUNTING!\n")
        time.sleep(2)