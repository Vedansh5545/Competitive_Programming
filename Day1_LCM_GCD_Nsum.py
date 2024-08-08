'''
This program will give you the LCM, GCD and N sum of the given numbers.
'''

#import math

def n_sum(n):
    return n*(n+1)//2

#print(n_sum(5))
'''
def gcd(a,b):
    # return math.gcd(a,b)
    if b==0:
        return a
    return gcd(b,a%b)
'''
#print(gcd(10,15))

def lcm(a,b):
    # return a*b//gcd(a,b)

    #return a*b//math.gcd(a,b)

    if a>b:
        greater = a
    else:
        greater = b

    while True:
        if greater%a==0 and greater%b==0:
            lcm = greater
            break
        greater += 1
    return lcm

#print(lcm(10,15))

