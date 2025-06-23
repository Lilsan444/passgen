import sys
import random
import string
from colorama import Fore, Back, Style

print(Fore.WHITE, "passgen by Lilsan444")
print(Fore.WHITE, "github: https://github.com/Lilsan444")
print(Style.RESET_ALL)
length = int(input("how long is the pass: "))

char = string.ascii_letters + string.digits + string.punctuation

GenPass = ''.join(random.choices(char, k=length))
print(Back.WHITE, Fore.BLACK, GenPass)
print(Style.RESET_ALL)

    
    

