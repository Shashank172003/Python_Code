s1 = input("Enter the first string: ")

lower = ''
upper = ''

for x in s1:
    if x.islower():
        lower += x
    else:
        upper += x

s2 = lower + upper

print(s2)
# The above code will convert the string to lowercase and uppercase. The lower() method converts all the characters in the string to lowercase, while the upper() method converts all the characters in the string to uppercase.