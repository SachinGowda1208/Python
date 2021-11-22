
def count_number_of_digits():
    org_num = int(input('Enter a number to count the number of digits->'))
    copy_num = org_num
    count_of_digits = 0
    
    while copy_num > 0:
        copy_num //= 10
        count_of_digits += 1

    print(f'{org_num} has {count_of_digits} num of digits')


