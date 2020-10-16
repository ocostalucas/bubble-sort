# Bubble Sort version 3
import main
import time
import psutil
import os

start = time.time()
process = psutil.Process(os.getpid())

list = main.read_file(10000)
comparisons = 0
exchanges = 0

j = 1
swap = True
while j <= len(list) and swap:
    swap = False
    for i in range(len(list)-1):
        comparisons+=1
        if list[i] > list[i+1]:
            exchanges+=1
            swap = True
            aux = list[i]
            list[i] = list[i+1]
            list[i+1] = aux
    j+=1

runtime = (time.time() - start)*1000

print('Quantidade de quantidade de comparações: ', str(comparisons))
print('Quantidade de trocas: ', str(exchanges))
print('Tempo de execução: ', str(runtime))
print('Uso da CPU: ', str(process.cpu_percent()),'%')
print('Uso da memória: ', str(process.memory_percent()),'%')