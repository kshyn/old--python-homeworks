N = 0
D = 0
while N < 10000:
    N1 = (N // 1000) - (N % 10)
    N2 = (N % 100 // 10) - (N % 1000 // 100)
    print('число', N, 'N1', N1, 'N2', N2, 0 ** abs(N2 + N1))
    D = D + (0 ** abs(N2 + N1))
    N = N + 1
print(D)
