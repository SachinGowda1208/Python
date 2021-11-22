# wap to find sum of all the digits of a number:-

num = int(input("Enter a number to find sum of digits ->"))

sum_of_digits = 0

while num > 0 :
    sum_of_digits = sum_of_digits + num % 10
    num = num //10

print('sum of digits', sum_of_digits)
    
 
