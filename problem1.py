#Given an array of size n-1 such thhat it only contains distinct integers in the range of 1 to n.Return Missing element
def missingelement(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i


n = int(input("Enter the input: "))
if 1 < n < 10 ** 6:
    arr = (input("Enter array: ").split())
    arr = [int(x) for x in arr]
    if 1 < len(arr) < n:
        if len(arr)==n-1:
            for x in arr:
                if not 0 < x < 10 ** 6:
                    print("Failed a[i] not matching constraint")
                    exit(0)
                if x not in range(1,n+1):
                    print("Value exceeded")
                    exit(0)


            print(missingelement(arr, n))
        else:
            print("array - not ")
    else:
        print(" Array size - greater than n-1")

else:
    print("Failed n not matching constraint")
