a = int(input("Enter the  num1:"))
b = int(input("Enter the num2:"))
print(f"Original Values\na={a}\nb={b}")
a = a + b
b = a - b
a = a - b
print(f"Swapped Values\na={a}\nb={b}")
