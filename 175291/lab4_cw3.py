import math

def mnozonator(*x):
    iloczyn = 1
    for a in x:
        iloczyn *= a
    return iloczyn

print(mnozonator(1,2,3,4,5))

def potegator(n, *liczby):
    suma = 0
    for x in liczby:
        suma += pow(x,n)
    return suma

print(potegator(3,3,3))

def mean(*liczby):
    wynik = sum(liczby) / len(liczby)
    return wynik

print(mean(1,2,3))

def gmean(*liczby):
    iloczyn = 1
    for a in liczby:
        iloczyn *= a
    iloczyn **= 1/len(liczby)
    return iloczyn
print(gmean(3,3,3))

def duzy_malyinator(*liczby):
    return max(liczby), min(liczby)

print(duzy_malyinator(5,2,1,4,6,8,9))





