import os
red='\033[31m'
green='\033[32m'
orange='\033[33m'
pink='\033[95m'
print(f"{orange}[~]install pakages!")
os.system("pkg install toilet -y ")
os.system("pkg install fish -y")
os.system("pkg install figlet -y ")
os.system("toilet -f mono12 -F gay bad-boy")
print(f"{pink}[1]1")
print("[2]2")
print("[3]3")
kinger = int(input("Enter : "))
if kinger == 1:
    joker = "toilet -f mono12 -F gay "
    os.system("clear")
    king = input(f"{green}Enter your text : ")
    os.system("clear")
    os.system(joker + king)
elif kinger == 2:
    os.system("clear")
    h=input(f"{green}Enter your text :  ")
    os.system("clear")
    os.system("toilet " + h)
    os.system("fish")
elif kinger == 3:
    os.system("clear")
    ko=input(f"{green}Enter your text : ")
    os.system("clear")
    os.system("figlet " + ko)
    os.system("fish")
