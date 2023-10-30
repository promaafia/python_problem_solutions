'''
	1.16.1. Write a program that read any binary number and display equivalent decimal number	
'''

n = int(input('Enter a binary number: '))
decimal = 0
power = 1
while n > 0:
    rem = n % 10
    n = n // 10
    decimal = decimal + (rem * power)
    power = power * 2
print('Equivalent decimal is: ', decimal)

'''
input = 0001
output = 1
input = 1011
output = 11
input = 101101
output = 45
'''
