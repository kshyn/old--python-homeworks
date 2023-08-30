n = int(input())
n1 = 0
x = 1
x1 = 1
while n != 0:
    if n == n1:
        x += 1
        if x > x1:
            x1 = x
    elif n != n1:
        x = 1
    n1 = n
    n = int(input())
print(x1)
