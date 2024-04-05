import math
names = ['michal', 'nela', 'ola', 'przemek']
names2 = [x.capitalize() for x in names]
names3 = [x for x in names if 'l' in x]
names4 = tuple([x.capitalize() for x in names if 'a' == x[-1]])
lenght = sum(len(x) for x in names)

print(names2)
print(names3)
print(names4)
print(lenght)