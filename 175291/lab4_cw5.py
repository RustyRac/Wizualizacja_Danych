pesel = '0207080362'

miesiace = {'styczeń': 1, 'luty': 2, 'marzec': 3, 'kwiecień': 4, 'maj': 5, 'czerwiec': 6, 'lipiec': 7, 'sierpień': 08, 'wrzesień': 09, 'październik': 10, 'listopad': 11, 'grudzień': 12}


def stuleciator(numer):
    num1 = numer[2]
    elif num1 in [8, 9]:
        stulecie = '18'
        miesiac = miesiace[80-int(numer[2:4])]
    elif num1 in [0, 1]:
        stulecie = '19'
        miesiac = miesiace[80 - int(numer[2:4])]
    elif num1 in [2, 3]:
        stulecie = '20'
        miesiac = miesiace[80 - int(numer[2:4])]
    elif num1 in [4, 5]:
        stulecie = '21'
        miesiac = miesiace[80 - int(numer[2:4])]
    elif num1 in [6, 7]:
        stulecie = '22'
        miesiac = miesiace[80 - int(numer[2:4])]
    else:
        return False

    return num
print(stuleciator(pesel))

def PESLATOR(numer):
    if not len(numer) != 11 and numer.isnumeric():
        return False










    print(f'{stulecie}{numer[0:2]}')
