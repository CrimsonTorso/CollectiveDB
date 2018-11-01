#!/usr/bin/python

import os
import module

responce = os.system("clear")
print('[!] Coded By CrimsonTorso [!]\n')
print('Welcome to dbZearcher')
print('1 - Search')
print('2 - Quit')
numSelect = raw_input('Please input a number: ')
if numSelect == '1':
	module.num1()
elif numSelect == '2':
	module.num2()