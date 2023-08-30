percent = int(input())
rubli = int(input())
copeyki = int(input())
vklad = rubli * 100 + copeyki
K = int(input())
year = 0
while K > 0:
    vklad = vklad + int((percent * vklad) / 100)
    K = K - 1
rubli = vklad // 100
copeyki = vklad % 100
print(rubli, copeyki)
