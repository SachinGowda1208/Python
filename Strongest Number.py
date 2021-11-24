from math import factorial

def start():
    num = int(input('Enter a number : '))
    is_strong(num)


def strong(num:int)-> int:
    res = 0
    while num > 0 :
        last_digit = get_last_digit(num)
        res = add(res, factorial(last_digit))
        num = remove_last_digit(num)
    return res
def get_last_digit(num:int)->int:
    return num % 10

def add(num1:int, num2:int)->int:
    return num1 + num2

def remove_last_digit(num):
    return num // 10

def is_strong(num:int):
    if  num == strong(num):
        print(f'{num} is an strong number ')
    else :
        print(f'{num} is not an strong number')




