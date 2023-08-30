# the program asks the user for integers until he writes "done".
# after the program will display the largest and smallest numbers from the entered

largest = None
smallest = None
while True:
    income = input('Input next number or "done" to end of the loop')
    if income == 'done':
        break
    else:
        try:
            income = int(income)
            if largest == None:
                largest = income
                smallest = income
            else:
                if income > largest:
                   largest = income
                if income < smallest:
                   smallest = income
        except ValueError:
            print('Invalid input')
print("Maximum is", largest)
print("Minimum is", smallest)
