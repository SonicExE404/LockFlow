import os
from colorama import Fore, Style, init
init() 

lgo = """
         _               _    
        | |    ___   ___| | __
        | |   / _ \\ / __| |/ /
        | |__| (_) | (__|   < 
        |_____\\___/ \\___|_|\\_\\
      .---.
     /    |\\________________     _____ _              
    |  ()  | ________   _   _)  |  ___| | _____      __                
     \\    |/        | | | |     | |_  | |/ _ \\ \\ /\\ / /
      `---'         "-" |_|     |  _| | | (_) \\ V  V /
                                |_|   |_|\\___/ \\_/\\_/ 

"""

print(Fore.BLUE + lgo + Style.RESET_ALL + Fore.RED+"                   LockFlow -- By SonicExE404\n"+Style.RESET_ALL)
print(Fore.LIGHTCYAN_EX + "\t[1] EzCrypt\n\t[2] Pass-Meter" + Style.RESET_ALL)
choose = input("What do you want to use :")

if choose == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    leet_dict = {
    "A": ["@"],
    "B": ["8"],
    "C": ["("],
    "D": ["|)"],
    "E": ["3"],
    "F": ["|="],
    "G": ["6"],
    "H": ["#"],
    "I": [ "!"],
    "K": ["|<"],
    "L": ["1"],
    "M": ["/\\/\\"] ,
    "N": ["|\\|"],
    "O": ["0"],
    "P": ["|°"],
    "R": ["|2"],
    "S": ["$"],
    "T": ["7"],
    "U": ["|_|"],
    "V": ["\\/"],
    "W": ["\\/\\/"],
    "X": ["><"],
    "Y": ["`/"],
    "Z": ["2"]
    }
    leet_dict_str = """
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "|=",
    "G": "6",
    "H": "#",
    "I": "!",
    "K": "|<",
    "L": "1",
    "M": "/\\/\\",
    "N": "|\\|",
    "O": "0",
    "P": "|°",
    "R": "|2",
    "S": "$",
    "T": "7",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "><",
    "Y": "`/",
    "Z": "2"
    """
    log = """
    d88888b d88888D  .o88b. d8888b. db    db d8888b. d888888b 
    88'     YP  d8' d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~' 
    88ooooo    d8'  8P      88oobY'  `8bd8'  88oodD'    88    
    88~~~~~   d8'   8b      88`8b      88    88~~~      88    
    88.      d8' db Y8b  d8 88 `88.    88    88         88    
    Y88888P d88888P  `Y88P' 88   YD    YP    88         YP    
                                                                                                              
    """
    print(Fore.GREEN + log + Style.RESET_ALL)
    def changer(passwd):
        output = passwd
        for i in output:
            if i.upper() in leet_dict:
                output = output.replace(i,leet_dict[i.upper()][0])
        return output

    while True:
        q1 = input("[1] Transform\n[2] Show List\n\nChoose : ")
        if q1 == "1":
            pass_before = input("Enter your password to transform: ")
            print(changer(pass_before))
        elif q1 == "2":
            print(leet_dict_str)

elif choose == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = 1
    upperList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowerList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    symbolsList = ["!","@","#","$","%","^","&","*","(",")","_","+","=","[","]","{","}","|",":",";","<",">","?","~","`","/","",".",",","-"]
    numList = ["0","1","2","3","4","5","6","7","8","9"]
    print(Fore.RED + """
     ███████████                                       ██████   ██████           █████                      
    ░░███░░░░░███                                     ░░██████ ██████           ░░███                       
     ░███    ░███  ██████    █████   █████             ░███░█████░███   ██████  ███████    ██████  ████████ 
     ░██████████  ░░░░░███  ███░░   ███░░   ██████████ ░███░░███ ░███  ███░░███░░░███░    ███░░███░░███░░███
     ░███░░░░░░    ███████ ░░█████ ░░█████ ░░░░░░░░░░  ░███ ░░░  ░███ ░███████   ░███    ░███████  ░███ ░░░ 
     ░███         ███░░███  ░░░░███ ░░░░███            ░███      ░███ ░███░░░    ░███ ███░███░░░   ░███     
     █████       ░░████████ ██████  ██████             █████     █████░░██████   ░░█████ ░░██████  █████    
    ░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░░             ░░░░░     ░░░░░  ░░░░░░     ░░░░░   ░░░░░░  ░░░░░     
                                                                                                                                                                                                                         
    """+ Style.RESET_ALL)
    while True:
        password = input("Enter Your password Here --> " + Fore.CYAN)

        def checker(char , passwd):
            for i in passwd:
                s = 0
                while s < len(char):
                    if i == char[s]:
                        return True
                    else:
                        s += 1
            return False

        cases = [checker(upperList , password),
                    checker(symbolsList, password),
                        checker(numList , password),
                            checker(lowerList, password)]

        strength = 0
        if len(password) >= 8:
            strength += 2
        c = 0

        while c < 4 :
            if cases[c] == True:
                strength += 2
            c += 1

        container = ""
        value = strength
        b = 0

        while value > 0:
            value -= 1
            b += 1
        
        for i in range(0,b):
            container += Fore.GREEN + "■" + Style.RESET_ALL
        
        for k in range(0,10 - b):
            container += Fore.LIGHTBLACK_EX + "■" + Style.RESET_ALL
        
        print(Fore.RED + " strength        ------>        " + Style.RESET_ALL + "[" + container + "]" + Fore.GREEN + str(strength) + "/10" + Style.RESET_ALL)

    
