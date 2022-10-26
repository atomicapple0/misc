#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

import functools


def calculateCost(arr):
    
    @functools.lru_cache(maxsize=None)
    def helper(i,j):
        if j - i == 1:
            return 0, arr[i]
        elif j - i == 2:
            return arr[i] * arr[j-1], max(arr[i],arr[j-1])
        best = float("inf")
        for k in range(i+1,j):
            left, maxiL = helper(i,k)
            right, maxiR = helper(k,j)
            if k == i+1:
                score = arr[i] * maxiR + right
            elif k == j-1:
                score = arr[j-1] * maxiL + left
            else:
                score = left + right + maxiL * maxiR
            if score < best:
                best = score
        return best, max(arr[i:j])

    
    sol, _ = helper(0,len(arr))
    return sol
            
        

import math
import os
import random
import re
import sys


#
# Complete the 'formTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER t
#  3. INTEGER_ARRAY q
#
import functools

def formTeam(d, t, q):
    print(d,t,q)

    @functools.lru_cache(maxsize=None)
    def helperD(l):
        # .... T
        if l <= 0:
            return 0
        if l == 1:
            return 1
        count = 0
        for i in range(1,min(d,l+1)):
            count += helperT(l-i)
        return count
            
    @functools.lru_cache(maxsize=None)
    def helperT(l):
        # .... D
        if l <= 0:
            return 0
        if l == 1:
            return 1
        count = 0
        for i in range(1,min(t,l+1)):
            count += helperD(l-i)
        return count
    
    sol = []
    for qq in q:
        sol.append(helperD(qq+1) + helperT(qq+1))
    return sol
        
if __name__ == '__main__':

def maximalSquare(self, samples) -> int:
    rows = len(samples)
    cols = len(samples[0])
    
    for i in range(rows):
        for j in range(cols):
            samples[i][j] = int(samples[i][j])
    
    for idx in range((rows+cols) // 2):
        # go right, from min(i,cols) to cols
        i = min(idx,rows-1)
        for r in range(min(i,cols), cols):
            if i-1 >= 0 and r-1 >= 0 and samples[i][r] == 1:
                score = min(samples[i-1][r], samples[i][r-1], samples[i-1][r-1])
                samples[i][r] = 1 if score == 0 else score + 1
        i = min(idx,cols-1)
        # go down, from min(i+1,rows) to rows
        for d in range(min(i+1,rows), rows):
            if i-1 >= 0 and d-1 >= 0 and samples[d][i] == 1:
                score = min(samples[d-1][i], samples[d][i-1], samples[d-1][i-1])
                samples[d][i] = 1 if score == 0 else score + 1
    
    sol = 0
    for i in range(rows):
        for j in range(cols):
            sol = max(sol, samples[i][j])
    return sol * sol