''''Write a program to check whether the enter character is special character or not.
(special character statement Block must be in statement block)'''

ch=input('enter your character:')

if not('A'<=ch<='Z' or 'a'<=ch<='z'or '0'<=ch<='9'):
    print('it is special character')
else:
    print('yes it not special character')
