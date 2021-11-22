#armtrong number:-

#armstrong:- 153 = 1**3=1,5**3=125,3**3=27,1+125+27=153
def start():
    num = int(input("Enter a num "))
    is_armstrong(num)
    
def armstrong(num:int)->int:
    count_of_digit = count_the_digit(num)
    res = 0
    while num > 0:
        last_digit = get_last_digit(num)
        res = add(res, pow(last_digit, count_of_digit))
        num = remove_last_digit(num)
    return res

def count_the_digit(num:int)->int:
    count = 0
    while num>0 :
        num = remove_last_digit(num)
        count = count + 1
    return count

def get_last_digit(num:int)->int:
    return num%10

def add(num1:int, num2:int)->int:
    return num1+num2

def remove_last_digit(num:int)->int:
    return num //10

def is_armstrong(num:int)->int:
    if num == armstrong(num):
        print(f'{num} is armstrong')
    else:
        print(f'{num} is not armstrong')
