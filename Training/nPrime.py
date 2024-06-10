def isprime(num):
    flag = 0
    if num == 0 or num == 1:
        return False
    else:
        for x in range(2, num - 1):
            if num % x == 0:
                flag = 1
                break
        if flag == 1:
            return False
        else:
            return True


num = int(input("Enter the number"))
print("List of prime 1 - ",num)
for n in range(1, num + 1):
    if isprime(n):
        print(n)

