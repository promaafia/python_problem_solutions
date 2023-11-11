'''
    2.10. Write a program that read two numbers and display bitwise AND
'''
num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
print('Bitwise and: ', num1 & num2)


'''
input: 
Number1: 7
Number2: 5
output:
Bitwise and:  5

Explain: 
7 = 111
5 = 101
bitwise and: 101 means 5

truth table:
a   b   and or  xor
0   0   0   0   0
0   1   0   1   1
1   0   0   1   1
1   1   1   1   0

'''