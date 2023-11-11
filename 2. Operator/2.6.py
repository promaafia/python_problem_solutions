'''
    2.6. Write a program that read two integer and display remainder
'''
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

while num2 == 0:
    print('Second number is zero')
    num2 = int(input('Enter second number again: '))
print('remainder is: ', num1 % num2)