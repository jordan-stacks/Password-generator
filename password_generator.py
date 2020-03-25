import random
import string

password = ''
pass_len = None
affirmitive = ['Yes', 'yes', 'Y', 'y']
negative = ['No', 'no', 'N', 'n']

while True:
    pass_len = input('How many characters would you like your password to be? \n')
    if pass_len.isalpha():
        print('Please choose a password length of at least 8 characters')
    else:
        pass_len = int(pass_len)
        if pass_len < 8:
            print('Password length must be at least 8 characters')
        else:
            break

while True:
    pass_type = input('Would you like your password to include special characters?\n')
    if pass_type in affirmitive:
        pass_type = 'complex'
        break
    elif pass_type in negative:
        pass_type = 'simple'
        break
    else:
        print('Please answer yes or no')

if pass_type in ['complex']:
    temp = 0
    if temp < pass_len:
        password[temp] = random.choice(string.printable)
        temp = temp + 1

else:
    random.choice(string.ascii_leters)

print(password)
