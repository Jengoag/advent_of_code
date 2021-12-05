data = open("day_01_data.txt","r")
lista = data.read().split('\n')
lista_int = list(map(int, lista))

import math
list_mas = []

for mas in lista_int:
    while mas >6:
        mas = math.floor(mas / 3) - 2
        list_mas.append(mas)
   
print(sum(list_mas))