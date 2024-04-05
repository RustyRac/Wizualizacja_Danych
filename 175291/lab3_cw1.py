import math

# lis= [1]
# lis.append(2)
# lis
# [1, 2]
#
# lis.extend([1,2,3])
# lis
# [1, 2, 1, 2, 3]
#
# lis.insert(0,4)
# lis
# [4, 1, 2, 1, 2, 3]
#
# lis.remove(4)
# lis
# [1, 2, 1, 2, 3]
#
# lis.pop(3)
# 2
#
# lis.clear()
# lis
# []
#
# lis.count(1)
# 0
#
# lis=[1,2,3,7,5,3,1,2,3]
# lis.sort()
# lis
# [1, 1, 2, 2, 3, 3, 3, 5, 7]
# lis.reverse()
# lis
# [7, 5, 3, 3, 3, 2, 2, 1, 1]
# lis.copy()
# [7, 5, 3, 3, 3, 2, 2, 1, 1]

lis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# a

def potegator(n):
    list = []
    for a in range(n+1):
        list.append(a**5)
    return list

print(potegator(14))

def silniator(n):
    list = []
    for a in range(n + 1):
        list.append(math.factorial(a))
    return list

print(silniator(20))


def eulerator(n):
    list = []
    for a in range(n + 1):
        list.append(math.e**a)
    return list

print(eulerator(19))

nazwiska = ['Rożnowski', 'Małecki', 'Piotrowski', 'Ornacki', 'Broda']

def liczytator(nazw):
    list = []
    for n in nazw:
        list.append(len(n))
    return list

print(liczytator(nazwiska))

# c

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[10,20,30,40,50,60,70,80,90,100]

list3= list1 + list2
print(list3)

def dodawator(lis1,lis2):
    list = []
    if len(lis1) == len(lis2):
        for n in range(len(lis1)):
            list.append(lis1[n]+lis2[n])
    return list

print(dodawator(list1,list2))

miesiace = ['styczeń', 'luty', 'marzec',
            'kwiecień', 'maj', 'czerwiec',
            'lipiec', 'sierpień', 'wrzesień',
            'październik', 'listopad','grudzień']
#miesiace.sort()
#print(miesiace)
dic = {}
def numerator():
    dic = {}
    miesiace = ['styczeń', 'luty', 'marzec',
                'kwiecień', 'maj', 'czerwiec',
                'lipiec', 'sierpień', 'wrzesień',
                'październik', 'listopad', 'grudzień']
    for n in range(12):
        dic[miesiace[n]] = n + 1

    return dic

print(numerator())

def alfabetator(lista, litera):
    wynik = []
    for n in lista:
        if n[0] > litera:
            wynik.append(n)
    return wynik

print(alfabetator(nazwiska, 'N'))

def wypluwator(nazwiska):
    list = [i for i in nazwiska if len(i) > 6]
    return list

print(wypluwator(nazwiska))

def czysortator_tylny(lista):

    if lista == sorted(lista, reverse=True):
        return True
    else:
        return False


print(czysortator_tylny([4,3,2,1]))
print(czysortator_tylny([4,3,4,1]))

def potegator_pro(lista):
    wynik = [i**3 for i in lista]
    return wynik

print(potegator_pro(lis))
floaty = [1.2 , 2.3, 3.4, 4.5, 5.6]
def wymieniator(lista, n1, n2):
    if n2 is not float or n1 is not float:
        return
    for n in len(lista):
        if lista[n] == n1:
            lista.insert(n, n2)

    return lista

print(wymieniator(floaty, 1.2, 6.9))
































