s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) != len(s2):
    print("The strings are not anagrams.")
else:
    for x in s1:
        if x not in s2:
            print('the string are not anagrams')
            break
        else:
            print('the string is anagrams')
            break
# The above code will check if two strings are anagrams or not. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, "listen" and "silent" are anagrams.