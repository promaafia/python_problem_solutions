'''
    2.20. Write a program that read two numbers and display maximum using ternary operator
'''
num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
maximum = f'{num1} is maximum' if num1 > num2 else f'{num2} is maximum'
print(maximum)

'''
ternary operator:
Syntax: [on_ture statement] if [expression] else [on_false statement]
example:    maximum = a if a < b else b
            print(maximum)
'''