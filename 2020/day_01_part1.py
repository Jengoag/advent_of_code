data = open("day_01_data.txt","r")
lista = data.read().split('\n')
lista_int = list(map(int, lista))

from itertools import combinations_with_replacement

temp = combinations_with_replacement(lista_int, 2)
lista_num = list(map(list,temp))

for par in lista_num:
    sum_i = sum(list(par)) 
    if sum_i == 2020:
        print(par[0] * par[1])