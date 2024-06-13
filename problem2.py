#Given an array of size n-1 such thhat it only contains distinct integers in the range of 1 to n.Return Missing element
def missingelement(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i


arr = []
n = int(input("Enter the input: "))
if 1 < n < 10 ** 6:
    for i in range(1, n):
        arr.append(int(input()))
        if not 0 < arr[i] < 10 ** 6:
            print("Constraints - violated")
            exit(0)

        if arr[i] > n:
            print("Error- value greater")
            exit(0)

    print(missingelement(arr, n))

else:
    print("Failed n not matching constraint")
