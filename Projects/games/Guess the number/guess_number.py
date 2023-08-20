#!/usr/bin/python3
#MADE BY: mickeyhousee

import random
import os
import time

num_machine = random.randint(1, 10)

def clear_console():
    os.system('cls') # Change this to "clear" for linux OS


while True:
    user_input = input("Do You want to play number guessing game? Press 1 to play and 0 to quit: ")
    if user_input == '1':
        clear_console()
        print("\n\tWelcome To Number Guessing Game")
        num_guesses=int()
        num_user = ""
        while num_machine != num_user:
            clear_console()
            try:
                num_user = int(input('\nEnter a number between (and including ) 1-9 : '))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if num_machine == num_user:
                clear_console()
                print("You did it :) the number is ")
                guesses = "Got it right with {} tries".format(num_guesses)
                print(guesses)
            else:
                num_guesses += 1
                print("Wrong number :( ")
                time.sleep(1)
                clear_console()


    if user_input == '0':
        break



