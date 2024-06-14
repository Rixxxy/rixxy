def prime(num):
    flag = 0
    if num == 0 or num == 1:
        print(num, "is not prime")
    else:
        for x in range(2, num - 1):
            if num % x == 0:
                flag = 1
                break
        if flag == 1:
            print(num, "is not prime")
        else:
            print(num, "is prime")


num = int(input("Enter the number :"))
prime(num)
