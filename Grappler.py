#!/usr/bin/env python3

import core, os, time

core.welcome_banner()
core.author()
time.sleep(1.5)
user_input = raw_input("Please enter a search query: ")
responce = os.system("grep -i " + user_input + " *")
time.sleep(2.5)
