#For only nested if and elif

jhon = float(input("Enter the John's age: "))
Smith= float(input("Enter the Smith's age: "))
ajay = float(input("Enter the Ajay's age: "))#taking input from the user and type casting the next value 

if jhon>Smith and jhon>ajay :#setting to compare the statement 
    print("Jhon is elder")
elif Smith>ajay:             # replacing else and if with elif
    print("Smith is elder")
else:
    print("Ajay is elder")
        