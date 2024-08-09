'''
This script contains three functions:
1. prime(): Checks if a given number is prime.
2. divisor(): Finds all divisors of a given number.
3. divisor2(): Finds all divisors of a given number using a more efficient method.
'''
from math import *

def prime():
    n = int(input("Enter the number: "))
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")


def divisor():
    n = int(input("Enter the number: "))
    dict = []
    for i in range(1, n+1):
        if n % i == 0:
            dict.append(i)

    print(dict)

def divisor2():
    n = int(input("Enter the number:"))
    dict = set()
    for i in range(1, int(sqrt(n))+1):
        if n% i == 0:
            dict.add(i)
            if i != n//i:
                dict.add(n//i)
    dict = list(dict)
    dict.sort()
    print(dict)

prime()

divisor()

divisor2()