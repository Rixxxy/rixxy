arr = []
n = int(input("Enter the input: "))
if 2 <= n <= 10 ** 5:
    for i in range(0, n):
        arr.append(int(input()))
        if not 1 <= arr[i] <= 10**5:
            exit(0)
    arr.sort()
    print(arr[-2])