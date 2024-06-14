def sequences(array):
    global prev
    a = []
    seq = 1
    val = array[0]
    prev = val
    a.append(val)
    for i in range(1, len(array)):
        if array[i] - val > 0:
            seq += 1
            prev = val
            val = array[i]
            a.append(val)
        elif prev < array[i] < val:
            val = array[i]
            a.pop()
            a.append(array[i])
        else:
            pass

    print(a)
    return seq


# arr = input("Enter array : ").split()
# arr = [int(x) for x in arr]
# print(arr)
# print(sequences(arr))
arr = [1, 2, 1, 5]
print("array:", arr)
print(sequences(arr))

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print("array:", arr)
print(sequences(arr))
