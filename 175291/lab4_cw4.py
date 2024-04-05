

def funkcja(**staruch):
    for key,value in staruch.items():
        print(key)
        print(value)
    print("Mam na imie " + staruch['Imie'])


funkcja(Imie='Karol')

def numerator(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} ma numer {value}')
    return

numerator(Rupert='1',Johnny='2')


def zarobkoinator(**kwargs):
    suma = 0
    for key,value in kwargs.items():
        suma+= value
    return suma

print(zarobkoinator(styczen=1243, luty=2))


