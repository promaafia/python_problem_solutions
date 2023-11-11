'''
    4.5. Write a program that read three numbers and display maximum
'''

a = int(input('Enter a number1: '))
b = int(input('Enter a number2: '))
c = int(input('Enter a number2: '))

if a > b and a > c:
    print(f'{a} is maximum number')
elif b > a and b > c:
    print(f'{b} is maximum number')
else:
    print(f'{c} is maximum number')
    
    
'''
# we can also find maximum number by using max() function
print('Maximum Number is: ', max(a, b, c))
'''