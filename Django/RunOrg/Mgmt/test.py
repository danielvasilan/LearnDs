import math
from decimal import Context,ROUND_HALF_DOWN, setcontext, Decimal

def is_prime(n):
    if (n == 2 or n == 3): 
        return True
    if (n < 2 or n%2 == 0): 
        return False
    if (n < 9): 
        return True
    if (n%3 == 0): 
        return False
    r = int(n**0.5)
    f = 5
    while (f <= r):
        if (n%f == 0): 
            return False
        if (n%(f+2) == 0): 
            return False
        f +=6
    return True   

setcontext(Context(prec=300))
xe = Decimal(1).exp()
xe_s = str(xe)

print(xe_s)

pos = 0
while (pos < 290):
    nr = int(xe_s[pos+2:pos+10])
    pos += 1
    if (is_prime(nr)):
        print(str(nr) + ":" + str(pos))
