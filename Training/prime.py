#according to math--literal
def prime(num):
    count = 0
    for n in range(1, num):
        if num % n == 0:
            count += 1
    if count == 2:
        print(num, "is prime")
    else:
        print(num, "is not prime")


num = int(input("Enter the number :"))
prime(num)
