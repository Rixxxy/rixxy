def print_numbers(i, n):
    if i > n:
        return
    else:
        print(i, end=" ")
        print_numbers(i + 1, n)


n = int(input("Enter the number: "))
print_numbers(1, n)
