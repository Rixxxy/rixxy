def find(arr,x):
    pos=[]
    for i in range(0,len(arr)):
        if arr[i]==x:
            pos.append(i)
    if pos:
        return pos
    else:
        return -1




arr = []
n = int(input("Enter the input: "))
if 1 <= n <= 10 ** 6:
    for i in range(0, n):
        arr.append(int(input()))
        if not 0 <= arr[i] <= 10**5:
            exit(0)
    x=int(input("Enter element to be found: "))
    if  0 <= x <= 10 ** 5:
        print(find(arr,x))

