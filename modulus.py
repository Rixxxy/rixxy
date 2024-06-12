def modulus(a, b):
    if b == 0:
        raise ValueError("0 cannot be divisor")

    # Work with positive values for the algorithm
    abs_a, abs_b = abs(a), abs(b)

    # Subtract b from a until a is less than b
    while abs_a >= abs_b:
        abs_a -= abs_b

    # Determine the sign of the remainder based on the original dividend
    return abs_a if a >= 0 else -abs_a


# Input handling
a = int(input("dividend: "))
b = int(input("divisor: "))

try:
    result = modulus(a, b)
    print("Remainder:", result)
except ValueError as e:
    print(e)
