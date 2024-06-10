a = int(input("Enter the  num1:"))
b = int(input("Enter the num2:"))
print(f"Original Values\na={a}\nb={b}")
temp = a
a = b
b = temp
print(f"Swapped Values\na={a}\nb={b}")
