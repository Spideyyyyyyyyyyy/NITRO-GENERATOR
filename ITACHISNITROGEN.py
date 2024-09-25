import random
import string
import requests
import os


RED = "\033[91m"
RESET = "\033[0m"  
CYAN = "\033[96m"  


def banner():
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(RED + """
    ███╗░░██╗██╗████████╗██████╗░░█████╗░
    ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗
    ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║
    ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║
    ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝
    ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░

    ░██████╗░███████╗███╗░░██╗
    ██╔════╝░██╔════╝████╗░██║
    ██║░░██╗░█████╗░░██╔██╗██║
    ██║░░╚██╗██╔══╝░░██║╚████║
    ╚██████╔╝███████╗██║░╚███║
    ░╚═════╝░╚══════╝╚═╝░░╚══╝

Nitro Code Generator - Spamming Discord gift codes...
    """ + RESET)

    
    print(CYAN + "Discord: itachi_420_.")  
    print("GitHub: https://github.com/Spideyyyyyyyyyyy/NITRO-GENERATOR.git")  
    print(RESET)  


def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(19))

class NitroGenerator:
    def __init__(self):
        banner()  
        self.codes = []
        self.check()

    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if data["message"] == 'Unknown Gift Code':
                print("Not Working: " +"https://discord.gift/"+ code)
            else:
                print("Possibly Working: " +"https://discord.gift/"+ code)
                with open("workedcodes.txt", "a+") as file:
                    file.write("\n"+ code)


NitroGenerator()
