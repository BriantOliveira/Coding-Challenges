# Hamming weight's 
# How many bits are set (high) in 0xfeedc0ffee? (How did you calculate it?)
# Answer is 29.

def bitcount(x):
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    return ((x * 0x0101010101010101) & 0xffffffffffffffff ) >> 56

#  In case the given number has most of the bits set to 0
def bitcount_zero(x):
    c = 0
    while x:
        x &= x - 1
        c += 1

    return c

def bitcount_py(x):
    return bin(x).count("1")

print(bitcount(0xfeedc0ffee))
print(bitcount_zero(0xfeedc0ffee))
print(bitcount_py(0xfeedc0ffee))