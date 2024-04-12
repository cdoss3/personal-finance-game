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
