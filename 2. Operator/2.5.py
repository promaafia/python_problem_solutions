'''
    2.5. Write a program that read two floating point numbers and divide them
'''
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

while num2 == 0:
    print('Second number is zero')
    num2 = int(input('Enter second number again: '))
print('div is: ', num1 / num2)