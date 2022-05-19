from random import randint
from fast_exponentiation import fast_pow

def find_quad_non_res(p, c):
    # p is a positive prime number
    # c is the max number of iterations
    # -999 means not found
    result = -999
    i = 0
    if p != 2:
        while ((i < c) and (result == -999)):
            a = randint(1, p-1)
            if ((fast_pow(a, ((p-1)/2)) % p) != 1):
                result = a
            i = i + 1
    return result, i

p = 17
c = 100
print(find_quad_non_res(p,c))

        
