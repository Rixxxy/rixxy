def divide(a, b):
    if b == 0:
        raise ValueError("Division by 0 not possible")


    a, b = abs(a), abs(b)

    quotient = 0
    while a >= b:
        a -= b
        quotient += 1

    if (a < 0) != (b < 0):
        return -a
    else:
        return a


a = int(input("dividend: "))
b = int(input("divisor: "))

try:
    result = divide(a, b)
    print("Result:", result)
except ValueError as e:
    print(e)
