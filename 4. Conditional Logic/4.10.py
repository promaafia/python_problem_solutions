'''
    4.10. Write a program that read any year and display its leap year or not
'''
while True:
    y = int(input('Enter years: '))
    if y % 4 == 0 or y % 400 == 0:
        print(f'{y} is leap year')
    elif y % 100 == 0:
        print(f'{y} is not leap year')
    else:
        print(f'{y} is not leap year')