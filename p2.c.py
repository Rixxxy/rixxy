arr = []
n = int(input("Enter the input: "))
if 1 <= n <= 10 ** 5:
    for i in range(0, n):
        arr.append(int(input()))
        if not 0 <= arr[i] <= n - 1:
            exit(0)
    c = []
    for i in range(0, n):
        if arr.count(i) > 1:
            c.append(i)
    if c:
        print(c)
    else:
        c.append(-1)
        print(c)
else:
    exit(0)
