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


    

calendar = ['Jan', 1, 1]

def next_day(calendar):
    """
    Advance the calendar by a day. Change month and year if necessary.

    Parameters
    ----------
    calendar : TYPE
        DESCRIPTION.

    Returns
    -------
    calendar : TYPE
        DESCRIPTION.

    """
    day = calendar[1]
    month = calendar[0]
    if day != 28:
        calendar[1] += 1
        return calendar
    else:
        if month == 'Jan':
            calendar[0] = 'Feb'
            calendar[1] = 1
        elif month == 'Feb':
            calendar[0] = 'Mar'
            calendar[1] = 1
        elif month == 'Mar':
            calendar[0] = 'Apr'
            calendar[1] = 1
        elif month == 'Apr':
            calendar[0] = 'May'
            calendar[1] = 1
        elif month == 'May':
            calendar[0] = 'June'
            calendar[1] = 1
        elif month == 'June':
            calendar[0] = 'July'
            calendar[1] = 1
        elif month == 'July':
            calendar[0] = 'August'
            calendar[1] = 1
        elif month == 'August':
            calendar[0] = 'Sept'
            calendar[1] = 1
        elif month == 'Sept':
            calendar[0] = 'Oct'
            calendar[1] = 1
        elif month == 'Oct':
            calendar[0] = 'Nov'
            calendar[1] = 1
        elif month == 'Nov':
            calendar[0] = 'Dec'
            calendar[1] = 1
        elif month == 'Dec':
            calendar[0] = 'Jan'
            calendar[1] = 1
            calendar[2] += 1

print('WELCOME TO PERSONAL FINANCE')
print()
print('(1) Print current status')
print('(2) Asset manager')
print('(3) Portfolio manager')
print('(4) Career manager')
print('(5) ')
print('(N) Start a new game')
print('(M) Bring up options menu')
print("Select an option by typing a number or letter. Type 'exit' to exit.")

n = True

while n:
    """Main program loop"""
    
    user_input = input("[PER FIN] ~ ").lower()
    
    match user_input:
        case '1':
            pfc.print_game_status(pc, calendar)
        case '2':
            print('(1) Add cash balance')
            print('(2) Subtract cash balance')
            asset_manager_choice = input('[ASS_MAN] ~ ')
            match asset_manager_choice:
                case '1':
                    how_much = int(input('How much? '))
                    pfc.add_cash(pc, how_much)
                    print("Your new balance is $" + str(pc.balance))
                case '2':
                    how_much = -int(input('How much? '))
                    pfc.add_cash(pc, -how_much)
                    print("Your new balance is $" + str(pc.balance))
        case '3':
            print('Not ready. Future stock market.')
        case '9':
            next_day(calendar)
            print('It is now ' + str(calendar))
        case 'm':
            print('(1) Print current status')
            print('(2) Asset manager')
            print('(3) Portfolio manager')
            print('(4) Career manager')
            print('(5) ')
            print()
            print('(N) Start a new game')
            print('(M) Bring up options menu')
            print()
        case 'n':
            pc = pfc.Student('Player', income=random.randint(30000, 70000), 
                         balance=random.randint(1000, 2000), assets={}, 
                         debt=random.randint(0, 5000), 
                         credit_score=random.randint(600,700))
        case _:
            print("ERROR: INVALID INPUT, please type a number, or type 'exit' to quit")