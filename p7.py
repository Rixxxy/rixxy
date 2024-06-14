def findTriplets(ar):
    found = False
    a = []
    for i in range(0, len(ar) - 2):
        for j in range(i + 1, len(ar) - 1):
            for k in range(j + 1, len(ar)):
                if ar[i] + ar[j] + ar[k] == 0:
                    found = True
                    a.append(ar[i])
                    a.append(ar[j])
                    a.append(ar[k])
                    print(a)
                    break
    if found:
        return 1
    else:
        return 0


arr = []
n = int(input("Enter the input: "))
if 1 <= n <= 10 ** 6:
    for i in range(0, n):
        arr.append(int(input()))

    print(findTriplets(arr))

arr=[0,-1,2,-3,1]
print(findTriplets(arr))
arr=[1,2,3]
print(findTriplets(arr))

#
# def findTriplets(arr):
#     found = False
#     i = 0
#     while i < len(arr) - 2:
#         j = i + 1
#         while j < len(arr) - 1:
#             k = j + 1
#             while k < len(arr):
#                 if arr[i] + arr[j] + arr[k] == 0:
#                     found = True
#                     triplet = [arr[i], arr[j], arr[k]]
#                     print(triplet)
#                     # Remove elements in reverse order to avoid shifting issues
#                     arr.pop(k)
#                     arr.pop(j)
#                     arr.pop(i)
#                     # Restart loop
#                     i = -1  # Will be incremented to 0 at the end of the outer loop
#                     break
#                 else:
#                     k += 1
#             if i == -1:
#                 break
#             else:
#                 j += 1
#         i += 1
#     if found:
#         return 1
#     else:
#         return 0
#
#
# arr = []
# n = int(input("Enter the number of elements: "))
# if 1 <= n <= 10 ** 6:
#     for x in range(n):
#         arr.append(int(input()))
#     print(findTriplets(arr))
