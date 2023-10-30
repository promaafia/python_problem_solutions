'''
    1.10. Write a program that read any upper case character and display in lower case
'''

char = input('Enter uppercase character: ')

if 'A' <= char[0] <= 'Z':
    print('lower case is: ', chr(ord(char[0]) + 32))
else:
    print('Wrong Input')        