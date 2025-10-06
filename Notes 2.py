'''Write a program to print the last value of the list only if the first value of the list is an integer'''

i=eval(input('enter your list'))
if type(i[0])==int:
    print(i[-1], 'yes the first value is integer')
