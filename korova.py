n = int(input())
if not n == 11 and n % 10 == 1:
    print(n, 'korova')
elif not 11 <= n <= 14 and 0 < (n % 10) <= 4:
    print(n, 'korovy')
else:
    print(n, 'korov')
