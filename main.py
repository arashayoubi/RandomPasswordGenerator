import random

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+/*-'

try:
    password_digits = int(
        input('Enter the number of digits you need for your password: '))
    password = ''.join(random.sample(characters, password_digits))
    print('your password is = ' + password)
except:
    print('Please enter a valid number')
