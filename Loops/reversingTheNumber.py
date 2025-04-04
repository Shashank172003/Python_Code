n = int(input('Enter the no you want to reverse: '))

rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
  
print('Reversed number: ',rev)
