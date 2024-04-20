# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:53:11 2024

@author: cdoss
"""

import sys
import os
import random
cwd = os.getcwd()
sys.path.append(cwd)

import pfclasses as pfc # Student, Stock, generate_student
# import time

pc = pfc.Student("Player")
calendar = pfc.Calendar(13, 'Jan', 1)

def menu_options():
    print('WELCOME TO PERSONAL FINANCE')
    print()
    print('(1) Print current status')
    print('(2) Asset manager')
    print('(3) Portfolio manager')
    print('(4) Career manager')
    print()
    print('(9) Advance to next day')
    print()
    print('(N) Start a new game')
    print('(M) Bring up options menu')
    print('(Q) Quit game')
    print()
    print("Select an option by typing a number or letter. Press 'Enter' to advance to next day.")

menu_options()
n = True

while n:
    """Main program loop"""
    
    user_input = input("[PER FIN] ~ ").lower()
    
    match user_input:
        case '':
            calendar.next_day()
            if calendar.day == 14 or calendar.day == 28:
                paycheck = pc.income / 24
                print()
                print(f'Pay day! Added ${paycheck} to your cash balance')
                pc.add_cash(paycheck)
            pfc.print_game_status(pc, calendar)
        case '1':
            pfc.print_game_status(pc, calendar)
        case '2':
            print()
            print('(1) Add cash balance')
            print('(2) Subtract cash balance')
            print()
            asset_manager_choice = input('[ASS_MAN] ~ ')
            match asset_manager_choice:
                case '1':
                    how_much = int(input('How much? '))
                    pc.add_cash(how_much)
                    print("Your new balance is $" + str(pc.balance))
                case '2':
                    how_much = int(input('How much? '))
                    pc.sub_cash(how_much)
                    print("Your new balance is $" + str(pc.balance))
        case '3':
            print('Not ready. Future stock market.')
        case '4':
            print('Not ready. Future career manager.')
        case '9':
            calendar.next_day()
            if calendar.day == 14 or calendar.day == 28:
                pc.add_cash(pc.income / 24)
            pfc.print_game_status(pc, calendar)    
        case 'm':
            menu_options()
        case 'n':
            pc = pfc.Student('Player', income=random.randint(30000, 70000), 
                         balance=random.randint(1000, 2000), assets={}, 
                         debt=random.randint(0, 5000), 
                         credit_score=random.randint(600,700))
        case _:
            print("ERROR: INVALID INPUT, please type a number, or type 'exit' to quit")