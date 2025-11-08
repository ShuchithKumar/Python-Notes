'''Write a program to check whether the entered value is muteable or immutable'''

v=eval(input('enter your value:'))

if type(v)in(list,set,dict):
    print(v,'yes it is muteable')
else:
    print(v,'it is immutable')
