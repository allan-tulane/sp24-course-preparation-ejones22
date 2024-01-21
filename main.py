"""
CMPS 2200  Preparation
"""

import math

def myfunction(input):
  if str(input).isdigit():
    return int(input)+2
  elif input.isalpha():
    txt = input[::-1]
    return "reversed: " +txt
  else:
    return "length: " + str(len(input))






