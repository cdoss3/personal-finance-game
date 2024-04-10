# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:58:30 2024

@author: cdoss
"""
import random
import time

class Student:
    def __init__(self, name, income=random.randint(30000, 70000), 
                 balance=random.randint(-2000, 2000), assets={}, 
                 debt=random.randint(0, 5000)):
        self.name = name
        self.balance = balance
        self.income = income
        self.assets = assets
        self.debt = debt
        return None
    
    def randomize_income(self, min, max) -> None:
        self.income = random.randint(min, max)
        
    def randomize_balance(self, min, max) -> None:
        self.balance = random.randint(min, max)
    
    def generate_assets(self):
        rng = random.random()
        if rng > 0.98:
            self.assets.update({'house': 150000, 'car': 10000})
        elif rng > 0.9:
            self.assets.update({'car': 1000})
        elif rng > 0.7:
            self.assets.update({'car': 5000})
        elif rng > 0.3:
            self.assets.update({'car': 2000})
            
            
class Stock:
    def __init__(self, name, ticker, value, volatility):
        self.name = name
        self.ticker = ticker
        self.value = value
        self.volatility = volatility
    
    def get_daily_change(self, chg=random.uniform(-5,5)):
        pct = chg / 100
        self.value = self.value * (1 + pct)


def generate_student(name) -> None:
    loader = {}
    temp_student = Student(name, income=random.randint(30000, 70000), 
                 balance=random.randint(-2000, 2000), 
                 debt=random.randint(0, 5000), assets = [])
    loader[name.lower()] = [temp_student.income, temp_student.balance, temp_student.debt, temp_student.assets]
    return loader


# reference yearly income print(classroom['name'][0])
# reference bank balance print(classroom['name'][1])
# reference amt of debt print(classroom['name'][2])
# reference list of assets print(classroom['name'][3])
# reference specific tuple within list of assets print(classroom['name'][3][0])
# reference specific value within specific tuple within list of assets print(classroom['name'][3][0][1])

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