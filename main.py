from random import sample

def write_file(value):
    f = open('file_'+ str(value) +'.txt', 'w')
    numbers = sample(range(0, value), value)
    for item in numbers:
        f.write("%s\n" % item)
    f.close()

def read_file(value):
    f = open('file_'+ str(value) +'.txt', "r")
    data = f.read().split('\n')[:-1]
    f.close()
    return data

write_file(10)
print(read_file(10))
