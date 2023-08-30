import sys

N = int(sys.argv[1])
i = 1
print((N - 1) * ' ', '#', sep='')
while N != i:
    i += 1
    print((N - i) * ' ', i * '#', sep='')
