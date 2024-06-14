def leader(arr):
    n = len(arr)
    a = []
    lead = arr[n - 1]
    a.append(lead)
    for i in range(n-2,-1,-1):
        if lead<=arr[i]:
            lead = arr[i]
            a.append(lead)

    return a[::-1]


arr = []
n = int(input("Enter the input: "))
if 1 <= n <= 10 ** 6:
    for i in range(0, n):
        arr.append(int(input()))
        if not 0 <= arr[i] <= 10 ** 5:
            exit(0)

    print(leader(arr))
