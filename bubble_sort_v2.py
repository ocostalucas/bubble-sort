# Bubble Sort version 1
import main
import time
import psutil
import os

start = time.time()
pid = os.getpid()
py = psutil.Process(pid)
n = 20000
main.write_file(n)
lista = main.read_file(n)
comparisons = 0
exchanges = 0

def bubble_sort_2(lista):
    loops = len(lista) - 1
    print("processing ... ")
    for i in range(len(lista)):
        for j in range(loops, i, -1):
            if lista[j] < lista[j-1]:
                aux = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = aux
    print("finished")
    return lista

new_list = (bubble_sort_2(lista))
end = time.time()
runtime = round(end - start)

print('Lista Ordenada', new_list)
print("tamanho da lista", len(lista))
print('Quantidade de quantidade de comparações: ', str(comparisons))
print('Quantidade de trocas: ', str(exchanges))
print('Tempo de execução: ', str(runtime))
print('Uso da CPU: ', str(py.cpu_percent()),'%')
