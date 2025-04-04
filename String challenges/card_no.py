card_no = input("Enter your card number: ")

lastDigit = card_no[15::]

four = '*' * 4 + ' '

display = four * 3 + lastDigit

print(display)