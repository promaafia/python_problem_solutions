'''
    2.7. Write a program that read radius of a circle and display the area
'''
pi = 3.1416
radius = int(input('Enter radius: '))

while radius == 0:
    print('Radius is zero')
    radius = int(input('Enter radius again: '))
print('Radius is: ', pi * (radius ** 2))