data = open("day_01_data.txt","r")
lista = data.read().split('\n')
lista_int = list(map(int, lista))



count_increased = 0
sum_past = 0
sum_next = 0


for n in range(0,len(lista_int) - 3):
    sum_past = lista_int[n] + lista_int[n+1] + lista_int[n + 2]
    sum_next = lista_int[n+1] + lista_int[n+2] + lista_int[n + 3]
    
    if sum_past < sum_next:
        count_increased += 1

print(count_increased)