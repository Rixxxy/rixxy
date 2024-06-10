n = int(input("Enter the number of row:"))
for i in range(1, n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i):
        print(" * ", end=" ")
    for j in range(n + i, n + n):
        print(" ", end=" ")
    print()

#inverted triangle
n = int(input("Enter the number of row:"))
for i in range(n-1, 0,-1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i):
        print(" * ", end=" ")
    for j in range(n + i, n + n):
        print(" ", end=" ")
    print()
