'''
    2.16. Write a program that read a number and mod by four using bitwise AND
'''
while True:
    num = int(input('Enter a number: '))
    # modulus by n with AND - num & (n - 1)
    print('result after modulus by 4 is: ', num & 3)
