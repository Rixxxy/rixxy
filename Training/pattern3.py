n = int(input("Enter the number"))
for i in range(0, n):
    for j in range(0, i):
        print("  ", end="  ")
    for j in range(i, i + 1):
        print(" * ", end="  ")
    for j in range(i + 1, n - i - 1):
        print("   ", end="  ")
    print()

n = int(input("Enter the number"))
for i in range(n - 1, -1, -1):
    for j in range(0, i):
        print("  ", end="  ")
    for j in range(i, i + 1):
        print(" * ", end="  ")
    for j in range(i + 1, n - i - 1):
        print("   ", end="  ")
    print()
