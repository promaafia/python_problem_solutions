'''
    4.6. Write a program that read three numbers and display minimum
'''
a = int(input('Enter a number1: '))
b = int(input('Enter a number2: '))
c = int(input('Enter a number2: '))

if a < b and a < c:
    print(f'{a} is minimum number')
elif b < a and b < c:
    print(f'{b} is minimum number')
else:
    print(f'{c} is minimum number')

'''
# we can also find minimum number by using min() function
print('minimum Number is: ', min(a, b, c))
'''