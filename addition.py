def divide(a, b):
    if b == 0:
        raise ValueError("Division by 0 not possible")

    negative_result = (a < 0) != (b < 0)
    a, b = abs(a), abs(b)

    quotient = 0
    while a >= b:
        a -= b
        quotient += 1

    if negative_result:
        return -quotient
    else:
        return quotient


def add_without_plus(a, b):
    while b != 0:
        # Calculate sum without considering carry
        sum_without_carry = a ^ b

        # Calculate carry
        carry = (a & b) << 1

        # Update a and b for the next iteration
        a = sum_without_carry
        b = carry

    return a




# Example usage
result = add_without_plus(2, 3)
print("Sum:", result)  # Output: Sum: 5

# Input handling
a = int(input("dividend: "))
b = int(input("divisor: "))

try:
    result = divide(a, b)
    print("Result:", result)
    result = add_without_plus(a, b)
    print("Result:", result)
except ValueError as e:
    print(e)
