#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pilesOfBoxes' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY boxesInPiles as parameter.
#

def pilesOfBoxes(boxesInPiles):

    boxesInPiles.sort(key=lambda x:-1*x)
    
    shortest = boxesInPiles[-1]

    acc = 0
    prev = boxesInPiles[0]
    for i,curr in enumerate(boxesInPiles):
        if i == 0:
            continue
        if curr == shortest:
            acc += i
            break
        if curr != prev: # another layer
            acc += i
        prev = curr
    return acc
            
        

if __name__ == '__main__':