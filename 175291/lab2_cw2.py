str = "kiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiw"

str2 = "kiwiwi"

# str = "kiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwi"
# print(str[12])
# w

# str + "bananana"
# 'kiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwibananana'

# str * 2
# 'kiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwikiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwi'

# len(str)
# 36

# str.isnumeric()
# False
#
# str.endswith("wiwiwi")
# True
#
# str.swapcase()
# 'KIWIWIWIWIWIWIWIWIWIWIWIWIWIWIWIWIWI'


#b

def parzystator(str):
    temp = ''
    for n in range(0, len(str), 2):
        temp += str[n]
    return temp

print(parzystator(str))

def koncowkator(str, n = 1):
    return str[-n:]

print(koncowkator(str, 4))

def odwracator(str):
    return str[::-1]

print(odwracator(str))

def palindromonator(str):
    if str == str[::-1]:
        return True
    else:
        return False

print(palindromonator(str))

def dlugosciator(str1, str2):

    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
        return 'Stringi są równe'

print(dlugosciator(str,str2))
print(dlugosciator(str, str))

imie, dataUr = 'Adam', '20.02.2002'

def formatator(imie, dataUr):
    return "My name is %s. My date of birth is %s" % (imie, dataUr)

print(formatator(imie,dataUr))










