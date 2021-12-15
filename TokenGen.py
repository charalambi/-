import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.GREEN + """
╔═╦╦══╦══╦═╦══╗
╚╗║║╔╗║╔╗║║╠║║╝
╔╩╗║╠╣║╔╗║║╠║║╗
╚══╩╝╚╩══╩═╩══╝ token gen
""")

amount = input("tokens amount:")
 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(int(amount) + 0):

   first = ''.join((random.choice(chars) for i in range (24))) 
   second = ''.join((random.choice(chars) for i in range(6))) 
   third = ''.join((random.choice(chars) for i in range (27)))
   
   result = first + "." + second + "." + third
   
   
   output = open("output.txt", "a") 
   output.write(result + "\n")

   #coded by YABOI
   #pyhackers ontop ;) !nasa downed!
   #colorama lololol

