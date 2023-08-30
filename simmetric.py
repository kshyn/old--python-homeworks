number = int(input())
left = number // 100
right = (number % 10) * 10 + (number // 10) % 10
print(left - right + 1)
