data = open("day_01_data.txt","r")
lista = data.read().split('\n')
lista_int = list(map(int, lista))

import math
list_fuel = []

for mas in lista_int:
    fuel = math.floor(mas / 3) - 2
    list_fuel.append(fuel)


print(list_fuel)
print(sum(list_fuel))