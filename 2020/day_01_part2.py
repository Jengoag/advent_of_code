data = open("day_01_data.txt","r")
lista = data.read().split('\n')
lista_int = list(map(int, lista))

temp = combinations_with_replacement(lista_int, 3)
lista_num = list(map(list,temp))

for tri in lista_num:
    sum_i = sum(list(tri)) 
    if sum_i == 2020:
        print(tri[0] * tri[1] * tri[2])