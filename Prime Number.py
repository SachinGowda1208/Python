#prime Number or Not:-
#while loop

n= int(input('Enter a number -> '))
count = 0
i = 1
while (n>=i):
    if (n%i==0):
        count = count + 1
    i = i+1

if (count==2):
    print('prime number ')

else :
     print('Not a prime number')


'''
#for loop


def start():
    num= int(input('Enter a number -> '))
    count = 0

    for n in range(1, num+1):
        if num % n==0:
            count = count + 1
        n = n+1

    if (count==2):
        print('prime number ')

    else :
          print('Not a prime number')
'''

#range function
"""
num = 7
for n in range(1, num+1):
    print(n)
"""
'''
def count_of_factors(num:int)->int:
    
    count_of_factors_of_num = int()
    for n in range(1, num+1):
        if num % n == 0 :
            count_of_factor_of_num += 1
            
    return count_of_factor_of_num

def is_prime(num:int)->bool:
    if count_of_factors(num) == 2:return True
    else : return False
    
def start():
    num = int(input('Enter a num to find prime or not = '))
    print(is_prime(num))


'''
