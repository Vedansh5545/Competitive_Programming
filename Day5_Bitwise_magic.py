
# bitwise and operator & 
# bitwise or operator |
# bitwise xor operator ^
# bitwise not operator ~
# bitwise left shift operator <<
# bitwise right shift operator >>
# right shift operator is used to divide a number by 2
# left shift operator is used to multiply a number by 2

def multpow2(x, y):
    return x << y

def divpow2(x, y):
    return x >> y



def evenodd(n):
    if n & 1:
        print("Odd")
    else:
        print("Even")

evenodd(5)

print(multpow2(5, 2))

print(divpow2(5, 2))