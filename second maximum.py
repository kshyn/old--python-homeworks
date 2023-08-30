n = int(input())
M1 = 0
M2 = 0
while n != 0:
    if n > M1:
        M2 = M1
        M1 = n
    elif n > M2:
        M2 = n
    n = int(input())
print(M2)
