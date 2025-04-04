pass1 = input("Enter your password: ")
pass2 = input("Confirm your password: ")
 
 
if pass1 == pass2:
     print("Password confirmed")
else:
    if pass1.casefold() == pass2.casefold():
        print("Password is case-insensitive")
    else: 
        print("Password mismatch")