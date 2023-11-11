'''
    4.12. Write a program to input any character and check whether it is alphabet, digit or special character
'''
while True:
    char = input('Enter character: ')
    # for capital letter
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        print(f'{char} is a alphabet')
    elif '0' <= char <= '9':
        print(f'{char} is a digit')
    else:
        print('special character')
