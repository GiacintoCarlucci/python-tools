from os import system
from sys import stdout, exit

system('clear')
GREEN,RESET = '\033[92m','\033[0m'

print(GREEN)
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("█▀▄▄▀█ ██ █▄ ▄█ ████▀▄▄▀█ ▄▄▀███▄ ▄█▀▄▄▀█▀▄▄▀█ ██ ▄▄")
print("█ ▀▀ █ ▀▀ ██ ██ ▄▄ █ ██ █ ██ ████ ██ ██ █ ██ █ ██▄▄▀")
print("█ ████▀▀▀▄██▄██▄██▄██▄▄██▄██▄████▄███▄▄███▄▄██▄▄█▄▄▄")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
print(RESET)

print("""

Select an option:

    {0}[{1}1{0}]{1}     First option
    {0}[{1}2{0}]{1}     Second option
    {0}[{1}0{0}]{1}     Exit

""".format(GREEN,RESET))

while True:
    try:
        ask = input("python-tools > ".format(GREEN,RESET))
        if ask.upper() == "1":
            print("you selected 1")
        if ask.upper() == "2":
            print("you selected 2")
        if ask.upper() == "0":
            exit(0)
    except:
        print("\nThank you for using python-tools.")
        exit(0)

