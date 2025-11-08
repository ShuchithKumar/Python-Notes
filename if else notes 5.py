'''Write a program to check whether the entered integer. Last digit is even or odd'''

i=int(input('enter your number'))
s=str(i)
if int(s[-1])%2==0:
    print('even number')
else:
    print('odd number')
