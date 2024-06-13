# def findTriplets(arr):
#     found = False
#     a = []
#     for i in range(0, len(arr) - 2):
#         for j in range(i + 1, len(arr) - 1):
#             for k in range(j + 1, len(arr)):
#                 if arr[i] + arr[j] + arr[k] == 0:
#                     found = True
#                     a.append(arr[i])
#                     a.append(arr[j])
#                     a.append(arr[k])
#                     print(a)
#                     break
#     if found:
#         return 1
#     else:
#         return 0
#arr = []
# n = int(input("Enter the input: "))
# if 1 <= n <= 10 ** 6:
#     for i in range(0, n):
#         arr.append(int(input()))
#
#     print(findTriplets(arr, n))


#
def findTriplets(arr):
    found = False
    i = 0
    while i < len(arr) - 2:
        j = i + 1
        while j < len(arr) - 1:
            k = j + 1
            while k < len(arr):
                if arr[i] + arr[j] + arr[k] == 0:
                    found = True
                    triplet = [arr[i], arr[j], arr[k]]
                    print(triplet)
                    # Remove elements in reverse order to avoid shifting issues
                    arr.pop(k)
                    arr.pop(j)
                    arr.pop(i)
                    # Restart loop
                    i = -1  # Will be incremented to 0 at the end of the outer loop
                    break
                else:
                    k += 1
            if i == -1:
                break
            else:
                j += 1
        i += 1
    if found:
        return 1
    else:
        return 0


arr = []
n = int(input("Enter the number of elements: "))
if 1 <= n <= 10 ** 6:
    for x in range(n):
        arr.append(int(input()))
    print(findTriplets(arr))
