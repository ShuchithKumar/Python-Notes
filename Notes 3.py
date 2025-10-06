'''Write a program to print the first character of the string, only if the first character is uppercase'''

s=input('enter your string')
if 'A'<=s[0]<='Z': #if s[0]>='A' and s[0]<='Z':
    print(s[0],'yes 1st character is upper case')
