dividend = int(input('enter the expected dividend yield in percentage points'))
rubli = int(input('enter ruble'))
copeyki = int(input('enter pennies'))
vklad = rubli * 100 + copeyki
dop = int(input('enter the amount of rubles to be contributed each year')) * 100
K = int(input('number of years'))
year=25
while K > 0:
     vklad = vklad + int((dividend * vklad) / 100) + dop
     K = K - 1
     year = year + 1
     if year > 40:
         dop = ((100 - ( 5 * (year - 40))) * dop) // 100
rubli = vklad // 100
copeyki = vklad % 100
print('shares savings', rubli, copeyki)
print('dividends received every month by the moment of termination of investments in shares in rubles',
       vklad * dividend / 10000 / 12)
