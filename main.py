from random import sample

def write_file(value):
    f = open('file_'+ str(value) +'.txt', 'w')
    numbers = sample(range(0, value), value)
    for item in numbers:
        f.write("%s\n" % item)
    f.close()

write_file(10)
