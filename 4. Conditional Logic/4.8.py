'''
    4.8. Write a program that read mark and display pass or fail
'''
while True:
    marks = int(input('Enter marks: '))
    if 0 <= marks <= 32:
        print('Fail')
    elif 33 <= marks <= 100:
        print('Pass')
    else:
        print('Invalid Input')