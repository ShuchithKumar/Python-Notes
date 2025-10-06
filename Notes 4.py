'''Write a program to print the first character, only if the ASCII value of that character is even'''

i=input('enter your character')
if ord(i[0])%2==0:
    print('yes', i[0], '''and it's ASCII value is''', ord(i[0]))
