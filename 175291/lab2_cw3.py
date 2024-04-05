
str = 'W Roku Pańskim 1345, Władca Hentyk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków.'
print(str.split())

def wyluskator(str):
    temp = ''
    suma = 0
    for n in range(len(str)):
        if str[n].isnumeric() or str[n] == '-' or str[n] == ' ':
            temp += str[n]
    list = temp.split()
    for n in list:
        suma += int(n)

    return suma, list

print(wyluskator(str))
