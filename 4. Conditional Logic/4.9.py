'''
    4.9. Write a program that read mark and display result in grade
'''
while True:
    marks = int(input('Enter marks: '))
    if 0 <= marks <= 32:
        print('Fail')
    elif 33 <= marks <= 39:
        print('D')
    elif 40 <= marks <= 49:
        print('C')
    elif 50 <= marks <= 59:
        print('B')
    elif 60 <= marks <= 69:
        print('A-')
    elif 70 <= marks <= 79:
        print('A')
    elif 80 <= marks <= 100:
        print('A+')
    else:
        print('Invalid Input')