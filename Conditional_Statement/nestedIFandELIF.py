
# for nested if and else 

jhon = float(input("Enter the John's age: "))
Smith= float(input("Enter the Smith's age: "))
ajay = float(input("Enter the Ajay's age: "))

if jhon>Smith and jhon>ajay :
    print("Jhon is elder")
else:
    if Smith>ajay:
        print("Smith is elder")
    else:
        print("Ajay is elder")
        