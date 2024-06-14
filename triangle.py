#inverted triangle
n = int(input("Enter the number of row:"))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print(i-j, end="   ")
    for j in range(n + i, n + n):
        print(" ", end=" ")
    print()
