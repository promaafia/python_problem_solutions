'''
    4.13. Write a program to check whether a character is uppercase or lowercase alphabet
'''
while True:
    alphabet = input('Enter a alphabet: ')
    if 'A' <= alphabet <= 'Z':
        print('uppercase alphabet')
    elif 'a' <= alphabet <= 'z':
        print('lowercase alphabet')
    else:
        print('Not a alphabet')
