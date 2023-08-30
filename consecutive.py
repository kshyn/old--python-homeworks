n = int(input()) #Maximum number of consecutive equal numbers
n1 = 0
x=1
x1 = 1
while n != 0:
     if n == n1:
         x += 1
         print(x)
     elif n != n1 and x > x1:
         x1 = x
         x=1
         print(x1)
     n1 = n
     n = int(input())
print(max(x, x1))
