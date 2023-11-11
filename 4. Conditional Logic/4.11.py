'''
    4.11. Write the code to check whether an input alphabet is a vowel or not. Both lower-case and upper-case should
      be checked
'''
while True:
    alphabet = input('Enter alphabet: ')
    # for capital letter
    if 'A' <= alphabet <= 'Z':
        if alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U':
            print(f'{alphabet} is a vowel')
        else:
            print(f'{alphabet} is a consonant')
    # for small letter
    elif 'a' <= alphabet <= 'z':
        if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
            print(f'{alphabet} is a vowel')
        else:
            print(f'{alphabet} is a consonant')

    else:
        print('Invalid character input')