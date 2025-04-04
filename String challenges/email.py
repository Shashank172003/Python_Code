emailId = input("Enter your email address: ")
atrate = emailId.find('@')  

print(atrate)

print('user name:', emailId[:atrate])
print('domain:', emailId[atrate+1:])
# The above code will print the user name and domain name of an email address.