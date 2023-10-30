'''
    1.9. Write a program that read any lower case character and display in upper case
'''

char = input('Enter lower case character: ')
if 'a' <= char[0] <= 'z':
    print('Upper case charecter is:', chr(ord(char[0])-32))
else:
    print('Wrong Input')
