s1 = input("Enter the first string: ")

for x in s1:
    if x in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        s1 = s1.replace(x, '')
print(s1)
# The above code will remove all the punctuation from the string. Punctuation is the use of spacing, conventional signs, and certain typographical devices as aids to the understanding and correct reading of written text.