'''
    4.16. Write a program to input angles of a triangle and check whether triangle is valid or not
'''
while True:
    print('Enter three angles: ')
    a, b, c = int(input()), int(input()), int(input())
    sum = a + b + c
    if sum == 180 and a > 0 and b > 0 and c > 0:
        print('Triangle is valid')
    else:
        print('Triangle is not valid')