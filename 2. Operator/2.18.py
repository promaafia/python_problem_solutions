'''
    2.18. Write a program to swap the values of two variables using temporary variable
'''
num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
temp = num1
num1 = num2
num2 = temp
print('After Swap Numbers:')
print('number1 is: ', num1, '\nnumber2 is: ', num2)