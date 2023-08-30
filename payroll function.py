def computepay(h, rate):
    if h <= 40:
        return rate * h
    else:
        return (rate * 40) + rate * 1.5 * (h - 40)
hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input('enter rate'))
p = computepay(h, rate)
print("Pay", p)
