n = int(input("Enter the value of n: "))

fact = 1

for count in range (1, n+1):
    fact = fact * count
    print ('factorial of number',n,'is',fact)