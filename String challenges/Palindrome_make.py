data = input("Enter a string: ")    

rev = data[::-1]

if data == rev: 
    print("The string is a palindrome.")
if data != rev:
    data = data + rev
    print(data)