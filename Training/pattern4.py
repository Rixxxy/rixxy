n = int(input("Enter an odd number for the size of X: "))

# Ensure n is an odd number
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
