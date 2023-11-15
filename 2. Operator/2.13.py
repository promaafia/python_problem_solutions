'''
    2.13. Write a program that read a number and divide by two using shift operator
'''
while True:
    n = int(input('Enter a number: '))
    print('result after divide by two: ', n >> 1)