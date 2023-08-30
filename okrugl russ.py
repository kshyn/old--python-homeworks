n = float(input())
rub = int(n)
if n < 0.5:
    rub -= 1
cop = int((n - rub) * 100)
if cop >= 50:
    rub += 1
    print(rub)
else:
    print(rub)
