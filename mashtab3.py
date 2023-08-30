n = int(input())
y = 1
if n % 2 != 0:
    while n > 0:
        y *= n
        n = n - 2
else:
    n -= 1
    while n > 0:
        y *= n
        n = n - 2
print(y)
