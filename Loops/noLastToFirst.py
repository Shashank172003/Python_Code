n = int(input('enter number : '))# type casting integer into the value 

while n > 0: 
    r = n % 10  # divide n by 10
    n = n // 10  # if given n value gives float as result upon dividing by 10 then convert it into the integer by using //
    print(r)
