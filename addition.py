def divide(a, b):
    if b == 0:
        raise ValueError("division 0 not allowed.")

    # Determine the sign of the result
    negative_result = (a < 0) != (b < 0)

    # Work with positive values for the algorithm
    a, b = abs(a), abs(b)

    quotient = 0
    while a >= b:
        a -= b
        quotient += 1

    return -quotient if negative_result else quotient


# Input handling
a = int(input("dividend: "))
b = int(input("divisor: "))

try:
    result = divide(a, b)
    print("Result:", result)
except ValueError as e:
    print(e)
