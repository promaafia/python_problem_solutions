'''
    4.18. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle
'''
side1 = int(input('Enter side1: '))
side2 = int(input('Enter side2: '))
side3 = int(input('Enter side3: '))

if side1 == side2 and side1 == side3:
    print('triangle is equilateral')
elif side1 == side2 or side2 == side3 or side1 == side3:
    print('triangle is isosceles')
else:
    print('triangle is scalene')
