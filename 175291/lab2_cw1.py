import math

print(math.floor(4.7))
print(math.ceil(4.4))
print(round(4.6))


def modulator(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a % b
    else:
        return math.fmod(a,b)

print(modulator(3, 7))
print(modulator(3.5, 7))

def logarator(a, n):
    for k in range(2, n+1):
        print(math.log(a, k), end=" | ")
    print("\n")

logarator(3, 10)

def multiplikator(a):
    return math.exp(a), math.e**a, math.pow(math.e, a)

print(multiplikator(4))

# math.pow(-1, 0)
# 1.0
# -1**0
# -1

# math.remainder(-10,3)
# -1.0
# -10%3
# 2

# a = (math.e**2 + math.e**(-2))/2
# b = (math.cosh(2))
# math.isclose(a,b)
# True





