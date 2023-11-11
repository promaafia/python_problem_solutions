'''
    2.12. Write a program that read two numbers and display bitwise Exclusive OR
'''
num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
print('Bitwise and: ', num1 ^ num2)


'''
input: 
Number1: 7
Number2: 5
output:
Bitwise xor:  2

Explain: 
7 = 111
5 = 101
bitwise and: 010 means 2

truth table:
a   b   and or  xor
0   0   0   0   0
0   1   0   1   1
1   0   0   1   1
1   1   1   1   0

'''