#!/usr/bin/env python

import sys

if __name__ == '__main__':
  max = int(sys.argv[1])

  nums = [True]*max

  for i in range(2,max):
    if nums[i]:
      for j in range(2*i, max, i):
        nums[j] = False
        
  for i in range(2,max):
    if nums[i]:
      print i
