n = int(input("Enter the number"))
for i in range(n):
    for j in range(0, n):
        if j == i or j == n - i - 1:
            print(" * ", end=" ")
        else:
            print("  ", end=" ")
    print()
