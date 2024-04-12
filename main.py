# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:53:11 2024

@author: cdoss
"""

import sys
sys.path.append('/home/redhorn/projects/personal-finance-project/personal-finance-game')

from pfclasses import Student
import time
import random

classroom = {}
n = True

while n:
    """Main program loop"""
    print('WELCOME TO PERSONAL FINANCE')
    print()
    print('(1) Generate new student')
    print('(2) Edit existing student')
    print('(3) Print current game state')
    print('(4) Export current game state')
    print('(5) Advance to the next day')
    print('')
    print("Select an option by typing a number. Type 'exit' to exit.")
    
    user_input = input("[PER FIN] ~ ")
    
    if user_input == '1':
        student_generator = True
        print("Chose to generate new student")
        time.sleep(2)
        while student_generator == True:
            new_student = input('[PER FIN] student-name ~ ')
            if new_student == 'done':
                student_generator = False
            else:
                classroom.update(generate_student(new_student))
    elif user_input == '2':
        print("Chose to edit current student")
        time.sleep(2)
    elif user_input == '3':
        print("Current game state:")
        for key, val in classroom.items():
            print(key.title() + ' has an income of $' + str(val[0]) + ', a bank balance of $' + str(val[1]) + ', owes $' + str(val[2]) + ', and owns ' + str(val[3]))
        time.sleep(2)
    elif user_input == '4':
        print("Chose to export game state")
        time.sleep(2)
    elif user_input == '5':
        print("Next day!")
        time.sleep(2)
    elif user_input == 'exit':
        print("Goodbye...")
        time.sleep(2)
        n = False
    else:
        print("ERROR: INVALID INPUT, please type a number, or type 'exit' to quit")
        time.sleep(2)
