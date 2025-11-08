#'''Write a program to check whether the entered integer number is even or odd'''

'''i=int(input('enter your integer:'))

if i%2==0:
    print(i,'it is even number')
else:
    print(i,'it is odd number')


'''

A=int(input('enter your integer:'))
flag=True

for i in range (2,A):
    if A%i==0:
        flag=False
        break
if flag:
    print('prime')
else:
    print('no')
