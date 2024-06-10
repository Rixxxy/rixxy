string = input("Enter the string :")
if string == string[::-1]:
    print("palindrome")
    print(string, "\n", string[::-1])
else:
    print("Not palindrome")
    print(string, "\n", string[::-1])
