# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:25:16 2021

@author: athan
"""

import random
rang = int(input('give me the range of the number'))
f= random.randint(1, rang)
tries = 0
for i in range(rang):
    tries += 1
    print(tries,'try')
    guess =int( input('guess a number'))
    if guess == f:
        print('success')
        break
    elif guess < f:
        print('give more powa')
    else:
        print('hold it back')

    