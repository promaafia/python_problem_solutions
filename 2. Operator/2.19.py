'''
    2.19. Write a program to swap the values of two variables without using temporary variable
'''
num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
print('After Swap Numbers:')
num1, num2 = num2, num1
print('number1 is: ', num1, '\nnumber2 is: ', num2)