import sys

digit_string = sys.argv[1]
# digit_string = input()
list_of_nums = list((digit_string[i:i+1] for i in range(0, len(digit_string), 1)))
for i in range(0, len(list_of_nums)):
    list_of_nums[i] = int(list_of_nums[i])
print(sum(list_of_nums))
sum(list_of_nums)
