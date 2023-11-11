'''
    2.21. Write a program that read two numbers and display minimum using ternary operator
'''
num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
minimum = f'{num1} is minimum' if num1 < num2 else f'{num2} is minimum'
print(minimum)

'''
ternary operator:
Syntax: [on_ture statement] if [expression] else [on_false statement]
example:    minimum = a if a < b else b
            print(minimum)
'''