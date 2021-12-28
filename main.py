#Password Generator

import random

print('Welcome To Password Generator')

#RANDOM CHARACTERS TO BE CHOSEN BY THE GENERATOR IN A STRING
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'

#the number of passwords we want to create
number = input('Amount of passwords to generate: ')
number = int(number)

#How long will your password be?
length = input('Your password length: ')
length = int(length)

print('/nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)