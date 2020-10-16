# Bubble Sort version 1
import main

list = main.read_file(10)
comparisons = 0
exchanges = 0


for i in range(len(list)):
    for j in range(len(list) - 1):
        comparisons += 1
        if list[j] > list[j+1]:
            aux = list[j]
            list[j] = list[j+1]
            list[j+1] = aux
            exchanges += 1

print('Quantidade de quantidade de comparações: ', str(comparisons))
print('Quantidade de trocas: ', str(exchanges))