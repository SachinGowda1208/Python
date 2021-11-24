#WAP to read stmt from file and reverse the stmt and print number of word in file:-

read = open('C:\\Users\\chiru\\Desktop\\Jspider-vibor\\file handling\\about shimog.txt', 'r')

line = read.read()
len(line)

for words in range(len(line)-1, -1, -1):
    print(line[words],end ='')

count = 1
for words in range(len(line)):
    if line[words] == " ":
        count +=  1

print(f'\n number words are {count}')

print(f' actucal words are = {line} and\n number of words are {count}')
