data = input("Enter a string: ")

rev = data[::-1]

if data == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# The above code will check if a string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. For example, "madam" is a palindrome.
# The code will take a string as input and reverse it. It will then compare the original string with the reversed string to check if they are the same. If they are the same, it will print "The string is a palindrome." Otherwise, it will print "The string is not a palindrome.".