from enum import auto
from ntpath import join
from pickle import TRUE
import random
from re import I
from tkinter import font
import colorama
from colorama import Fore
colorama.init(autoreset= True)
import time

print(Fore.BLUE+"""          ___/---CREATED BY Osmo-3---\___    """)
wordlist = "abcdefghijklnopqrstuvwxyz123456789@#$*-"
while True:
    q = int(input("enter password len:"))
    if q >= 1:
        break
    print("you have to enter a number above 0")

password = ""

password = random.choices(wordlist,k=q)

print("your password is:"+Fore.GREEN+"".join(password))
while True:
    ask = input("do you want to brute force your new password?(y/n):")
    if ask == "y" or ask == "n":
        break
    print("you have to type(y/n)")
if ask == "y":
    for i in range(3,0,-1):
        time.sleep(1)
        print(i)
    time.sleep(2)
    while True:
        brute = random.choices(wordlist,k=q)

        print(Fore.LIGHTGREEN_EX+str(brute))

        if brute == password:
            print("your passsowrd("+Fore.RED+"".join(password)+Fore.RESET+") have been found!")
            print("try again and make the password length above 6 to get a stronger pass")
            break
else:
    quit