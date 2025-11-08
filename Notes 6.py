'''Write a program to print the last character of the string, only if the ASCII value of that character is palindrome'''

r=input('enter your string')
if str(ord(r[-1]))==str(ord(r[-1]))[::-1]:
    print(r[1])
