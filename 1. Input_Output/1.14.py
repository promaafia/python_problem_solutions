'''
    1.14. Write a program that read any octal number and display equivalent decimal number
'''

octal_number = input('Enter a octal number: ')

print(f'{octal_number} is a octal number\n')

print('Decimal of octal number is: ', int(octal_number, 8))



'''
    input = 0o4
    output = 4
    
    input = 14
    output = 12
    
    input = 223
    output = 0o337
'''
