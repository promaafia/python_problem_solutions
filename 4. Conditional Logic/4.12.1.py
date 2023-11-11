'''
    4.12.1. Write a program to input any character and check whether it is alphabet, digit or special character using function
'''
while True:
    char = input('Enter character: ')
    if char.isalpha():
        print(f'{char} is a alphabet')
    elif char.isdigit():
        print(f'{char} is a digit')
    else:
        print('special character')