#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
  tip = calculate(meal_cost, tip_percent)
  tax = calculate(meal_cost, tax_percent)
  totalCost = int(round(meal_cost + tip + tax))
  print(totalCost)

def calculate(meal_cost, x):
  return meal_cost * (x/100)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
