# Bubble Sort version 1
import main
import time
import psutil
import os

start = time.time()
process = psutil.Process(os.getpid())

list = main.read_file(100)
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

runtime = (time.time() - start)

print('Quantidade de quantidade de comparações: ', str(comparisons))
print('Quantidade de trocas: ', str(exchanges))
print('Tempo de execução: ', str(runtime))
print('Uso da CPU: ', str(psutil.cpu_percent(interval=1)),'%')
print('Uso da memória: ', str(process.memory_percent()*100),'%')