#!/usr/bin/python3
#MADE BY: mickeyhousee

# TODO - ACABAR O RESTO DAS FUNÇÕES

import random
import os

def clear_console():
    os.system("cls")

def one():
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")

def two():
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[   0 ]")
    print("[-----]")

def three():
    print("[-----]")
    print("[     ]")
    print("[0 0 0]")
    print("[     ]")
    print("[-----]")



def roll_dice():
    while True:
        num = random.randint(1, 6)
        print(num)
        if num == 1:
            one()
            return
        if num == 2:
            two()
            return
        if num == 3:
            three()
            return
        else:
            print("Something went wrong :( )")
            break

clear_console()
while True:
    user_input = input("Press 1 to roll the dice or q to exit: ")
    if user_input == "1":
        clear_console()
        roll_dice()
    elif user_input == "q":
        exit()
    else:
        clear_console()
        print('Invalid Input')
