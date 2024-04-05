

liczby = {'1':'jeden','2':'dwa','3':'trzy','4':'cztery','5':'pięć',
          '6':'sześć','7':'siedem','8':'osiem','9':'dziewięć','0':'zero'}

print(liczby)
def zamieniator():
    tekst = str(input('Give text'))
    wynik = ''
    for x in tekst:
        if x in liczby:
            wynik += liczby[x] + ' '
    return wynik

print(zamieniator())
