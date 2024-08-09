
'''
This code generates prime numbers upto n using Seive Theorem
'''

from math import *

def seive(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False 
    for i in range(2, int(sqrt(n))+1): 
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    for i in range(2, n+1):
        if primes[i]:
            print(i, end=' ')

n = int(input())
seive(n)
