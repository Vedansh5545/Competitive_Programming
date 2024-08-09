

from math import sqrt

def approch1(n):
    """
    Approach 1:
    This function checks if a given number 'n' is prime.
    - It prints "Approach 1" and the number 'n'.
    - It initializes a counter 'divcnt' to count the number of divisors of 'n'.
    - It iterates from 1 to 'n' and increments 'divcnt' each time 'n' is divisible by 'i'.
    - If 'divcnt' equals 2 (meaning 'n' has exactly two divisors: 1 and itself), it prints "Prime".
    - Otherwise, it prints "Not Prime".
    - Finally, it prints an empty line for separation.
    """
    print("Approch 1")
    print(n)
    divcnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            divcnt += 1
    if divcnt == 2:
        print("Prime")
    else:
        print("Not Prime")
    print()

def approch2(n):
    '''
    Approach 2:
    This function checks if a given number 'n' is prime using a more optimized method.
    - It prints "Approach 2" and the number 'n'.
    - It immediately returns "Not Prime" for 0 and 1, as they are not prime numbers.
    - It immediately returns "Prime" for 2 and 3, as they are prime numbers.
    - (The rest of the function is not shown in the excerpt, but it likely includes further checks for primality.)
    '''
    print("Approch 2")
    print(n)
    if n == 0 or n == 1:
        print("Not Prime")
        return
    
    elif n == 2 or n == 3:
        print("Prime")
        return

    elif n % 2 == 0 or n % 3 == 0:
        print("Not Prime")
        return

    for i in range(5, int(sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            print("Not Prime")
            return
    print("Prime")
    print()


approch1(2)
approch2(2)
approch1(3)
approch2(3)
approch1(4)
approch2(4)
