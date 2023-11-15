'''
    2.15. Write a program that read a number and multiply by five using shift operator
'''
while True:
    n = int(input('Enter a number: '))
    print('result after multiply by two: ', (n << 2)+n)
