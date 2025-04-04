Amount = float(input("Enter bill amount: "))

if Amount<=1000:
    discount = Amount * 10 / 100
elif Amount>1000 and Amount <=5000 :
    discount = Amount * 20 / 100
elif Amount>5000 and Amount<=10000 :
    discount = Amount * 30 / 100 
else:
    discount = Amount * 50 / 100
    discameout = Amount - discount
    print("PAY", discameout)