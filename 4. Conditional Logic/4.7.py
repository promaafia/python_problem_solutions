'''
    4.7. Write a program that read three numbers and display median
'''
a = int(input('Enter a number1: '))
b = int(input('Enter a number2: '))
c = int(input('Enter a number2: '))

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print('Median is: ', median)