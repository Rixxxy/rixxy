def maximum(arr):
    m = arr[len(arr) - 1]
    for i in range(0, len(arr) - 1):
        if m < arr[i]:
            m = arr[i]
    return m


arr = []
n = int(input("Enter the input: "))
if 2 <= n <= 10 ** 5:
    for i in range(0, n):
        arr.append(int(input()))
        if not 1 <= arr[i] <= 10 ** 5:
            exit(0)
    m = maximum(arr)
    arr.remove(m)
    m = maximum(arr)
    print(m)
