#!/usr/bin/env python

import sys
import random

if __name__ == '__main__':
  target= random.randrange(1, 101)
  number = int(raw_input('Guess a number between 1 and 100: '))
  while number is not target:
    diff = abs(number - target)
    if diff < 2:
      print 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
    elif diff < 5:
      print 'HOT!'
    elif diff < 10:
      print 'A little too hot for comfort, no?'
    elif diff < 20:
      print 'Getting warmer...'
    elif diff < 30:
      print 'Meh...'
    else:
      print 'Cold'
    number = int(raw_input('Guess again: '))
  print 'Yatta! You got it!'
