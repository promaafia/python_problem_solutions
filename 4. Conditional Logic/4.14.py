'''
    4.14. Write a program to generate a simple arithmetic calculator
	hints:
	enter two numbers: 6 5
	select the menu:
	1. Add
	2. Subtract
	3. Multiply
	4. Divide
'''
while True:
    print('Enter two numbers: ')
    a, b = int(input()), int(input())
    print('Select the menu: ')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    n = int(input('Select Operation: '))
    if n == 1:
        print(f'Sum of {a} and {b} is: ', a + b)
    elif n == 2:
        print(f'Sub of {a} and {b} is: ', a - b)
    elif n == 3:
        print(f'Multiply of {a} and {b} is: ', a * b)
    elif n == 4:
        print(f'Div of {a} and {b} is: ', a / b)
    else:
        print('Please select from 1-4')
