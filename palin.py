number = int(input("Enter the number :"))
num = number
rev = 0
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

if rev == number:
    print(" palindrome\n", number, "\n", rev)
else:
    print("Not palindrome\n", number, "\n",rev)
