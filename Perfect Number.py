def start():
    n = int(input("Enter a number "))
    count = 0
    i = 1
    while n>i:
        if n%i==0:
            count = count + i
        i + i+1
    if n == count:
        print(f'given num {n} is perfect num')
    else:
        print(f'given num {n} is not perfect num')
