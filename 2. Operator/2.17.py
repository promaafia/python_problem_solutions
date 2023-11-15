'''
    2.17. Write a program that read a number and mod by eight using bitwise AND
'''
while True:
    num = int(input('Enter a number: '))
    # modulus by n with AND - num & (n - 1)
    print('result after modulus by 7 is: ', num & 7)
