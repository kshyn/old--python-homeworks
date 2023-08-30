n = int(input())
X = float(input())
y = 1
a = float(input())
if n == 0:
    print(a)
else:
    summa = a * X
    while y < n:
        a = float(input())
        summa = (summa + a) * X
        y = y + 1
    if y == n:
        a = float(input())
        summa = (summa + a)
    print(summa)
