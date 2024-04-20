# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:58:30 2024

@author: cdoss
"""
import random


class Student:
    def __init__(self, name, income=random.randint(30000, 70000), 
                 balance=random.randint(1000, 2000), assets={}, 
                 debt=random.randint(0, 5000), 
                 credit_score=random.randint(600,700)):
        self.name = name
        self.balance = balance
        self.income = income
        self.assets = assets
        self.debt = debt
        self.credit_score = credit_score
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
    
    def add_cash(self, amt):
        self.balance += amt
    
    def sub_cash(self, amt):
        self.balance -= amt


class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def next_day(self):
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
        
        if self.day != 28:
            self.day += 1
        else:
            if self.month == 'Jan':
                self.month = 'Feb'
                self.day = 1
            elif self.month == 'Feb':
                self.month = 'Mar'
                self.day = 1
            elif self.month == 'Mar':
                self.month = 'Apr'
                self.day = 1
            elif self.month == 'Apr':
                self.month = 'May'
                self.day = 1
            elif self.month == 'May':
                self.month = 'June'
                self.day = 1
            elif self.month == 'June':
                self.month = 'July'
                self.day = 1
            elif self.month == 'July':
                self.month = 'August'
                self.day = 1
            elif self.month == 'August':
                self.month = 'Sept'
                self.day = 1
            elif self.month == 'Sept':
                self.month = 'Oct'
                self.day = 1
            elif self.month == 'Oct':
                self.month = 'Nov'
                self.day = 1
            elif self.month == 'Nov':
                self.month = 'Dec'
                self.day = 1
            elif self.month == 'Dec':
                self.month = 'Jan'
                self.day = 1
                self.year += 1

            
class Stock:
    def __init__(self, name, ticker, value, volatility):
        self.name = name
        self.ticker = ticker
        self.value = value
        self.volatility = volatility
    
    def get_daily_change(self, chg=random.uniform(-5,5)):
        pct = chg / 100
        self.value = self.value * (1 + pct)


def add_cash(student, amount):
    student.balance += amount


def print_game_status(student, calendar):
    print()
    print('The date is ' + calendar.month + ' ' + str(calendar.day) + ', year ' + str(calendar.year))
    print(student.name + ' has $' + str(student.balance) + ' in the bank, makes $'
          + str(student.income) + ' per year, and owes $' + str(student.debt)
          + '\n')
    print()

def print_date(calendar):
    print()
    print('The date is ' + calendar.month + ' ' + str(calendar.day) + ', year ' + str(calendar.year) + '\n')
    print()


# reference yearly income print(classroom['name'][0])
# reference bank balance print(classroom['name'][1])
# reference amt of debt print(classroom['name'][2])
# reference list of assets print(classroom['name'][3])
# reference specific tuple within list of assets print(classroom['name'][3][0])
# reference specific value within specific tuple within list of assets print(classroom['name'][3][0][1])
