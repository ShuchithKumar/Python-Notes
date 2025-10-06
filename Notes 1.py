'''Write a program to print the character present at even index only if the string contains more than six characters'''

i=input('enter your string')
if len(i)>6:
    print(i[::2])
