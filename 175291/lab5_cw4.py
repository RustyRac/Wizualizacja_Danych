sym = ["M", "CM", "D", "CD",
       "C", "XC", "L", "XL",
       "X", "IX", "V", "IV", "I"]
val = [1000, 900, 500, 400,
       100, 90, 50, 40,
       10, 9, 5, 4, 1]
dic = {"M": 1000, "D": 500, "C": 100,
       "L": 50, "X": 10, "V": 5, "I": 1}


def romamama(number):
    temp = number
    roman_num = ''
    i = 0
    while number > 0:
        for n in range(number // val[i]):
            roman_num += sym[i]
            number -= val[i]
        i += 1
    return roman_num
print(romamama(130))
def arababa(s):
    numper = s
    temp = 0
    liczba = 0
    for i in numper[::-1]:
        if dic[i] >= temp:
            liczba += dic[i]
        else:
            liczba -= dic[i]
        temp = dic[i]
    return liczba

print(arababa('L'))

class Romanian:

    def __init__(self, litera):
        self.litera = litera
        self.liczba = arababa(litera)




    def __add__(self, other):
        return romamama(self.liczba+other.liczba)
    def __sub__(self,other):
        return romamama(self.liczba - other.liczba)
    def __mul__(self, other):
        return romamama(self.liczba * other.liczba)







a = Romanian('XIX')
b = Romanian("I")
print(a.liczba)
print(a+b)
print(a-b)
print(a*b)







