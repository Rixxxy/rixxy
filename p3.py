n = int(input("Enter n: "))
if 1 <= n <= 10 ** 9:
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print("Sum: ", total)

if 1 <= n <= 10 ** 9:
    t= n * (n + 1) // 2
    print(t)

