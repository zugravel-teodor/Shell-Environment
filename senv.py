# Welcome to the Shell Environment (SENV) ~ by Zugrăvel Teodor

# A highly customizable and EXTREMELY lightweight shell dashboard TUI.
# To open SENV every time you boot please add the fallowing line to your .bashrc/.zshrc: python3 /path/to/senv.py
# Feel free to delete every line of code you don't need.




from datetime import datetime # Needed to display time and date

import random # Only needed for the quote() plugin 

import getpass # Needed to display username

import time # Only needed for the  boot_anim() plugin

from colorama import Fore, init # Needed to display colors

import subprocess # Needed for basic system commands

import plugins # Only needed if you use any plugins




init()



username = getpass.getuser() # Gets username

temp = subprocess.check_output(["curl", "-s", "wttr.in?format=%t"]).decode().strip() # Gets temperature

while True:

    # Dashboard
    subprocess.run("clear", shell=True)
    print(f"{Fore.CYAN}███████ ███████ ███    ██ ██    ██{Fore.RESET}         Hello, {Fore.YELLOW}{username}{Fore.RESET}!")
    print(f"{Fore.CYAN}██      ██      ████   ██ ██    ██{Fore.RESET}         What would you like to do today ?")
    print(f"{Fore.CYAN}███████ █████   ██ ██  ██ ██    ██{Fore.RESET} ")
    print(f"{Fore.CYAN}     ██ ██      ██  ██ ██  ██  ██{Fore.RESET}       Time:   {Fore.YELLOW}|{Fore.RESET}      Date:       {Fore.YELLOW}|{Fore.RESET}    Weather:")
    print(f"{Fore.CYAN}███████ ███████ ██   ████   ████{Fore.RESET}      {Fore.GREEN}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}  {Fore.YELLOW}|{Fore.RESET}  {Fore.GREEN}  {datetime.now().strftime('%Y-%m-%d')}{Fore.RESET}  {Fore.YELLOW}  |{Fore.RESET}     {Fore.GREEN}{temp}{Fore.RESET}")
    print("                               ")
    print("         +--------------------------------------------------------------+")
    print(f"         | Roses are {Fore.RED}red{Fore.RESET}, violets are {Fore.BLUE}blue{Fore.RESET},   (GPLv3 reference hehe )   |")
    print(f"         | You use {Fore.CYAN}SENV{Fore.RESET}, you are now {Fore.GREEN}FREE{Fore.RESET}!    (Type li to learn more)   |")
    print("         +--------------------------------------------------------------+")
    cmd = input(">> ")

    # Commands

    # Quit
    if cmd == "q":
        subprocess.run("clear", shell=True)
        break

    # Vim
    elif cmd == "v":
        path = input("Path/file name >> ")
        subprocess.run(["vim", path])
    
    # pwd
    elif cmd == "d":
        subprocess.run(["pwd"])
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")
    
    # top
    elif cmd == "t":
        subprocess.run(["top"])
    
    # cat
    elif cmd == "c":
        path = input("Path/file name >> ")
        subprocess.run(["cat", path])
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")
    
    # touch
    elif cmd == "o":
        flname = input("file name >> ")
        subprocess.run(["touch", flname])
    
    # rm -rf
    elif cmd == "r":
        flname = input("file name/directory name >> ")
        subprocess.run(["rm", "-rf", flname])
    
    # mkdir
    elif cmd == "m":
        flname = input("directory name >> ")
        subprocess.run(["mkdir", flname])
    
    # ls
    elif cmd == "l":
        subprocess.run(["ls"])
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")
    
    # Weather
    elif cmd == "w":
        subprocess.run(["curl", "wttr.in"])
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")
    
    # Manual
    elif cmd == "man":
        print("Welcome to the Shell ENVironment manual!")
        print("Here you will learn the basics of SENV.\n")
        print("0.1: COMMANDS")
        print("---------------------------------------")
        print("q   - (exit) exits SENV")
        print("v   - (vim) opens the vim CLI text editor")
        print("d   - (pwd) prints current working directory")
        print("t   - (top) shows system information such as RAM usage and running processes")
        print("c   - (cat) prints current the contents of a file")
        print("o   - (touch) creates a file")
        print("r   - (rm -rf) removes a file or a directory. ")
        print("m   - (mkdir) creates a directory")
        print("l   - (ls) shows files and directories in the current working directory")
        print("w   - (curl wttr.in) shows weather information")
        print("man - (manual) you are now here")
        print("---------------------------------------\n")
        print("0.2: HOW TO USE THE COMMANDS")
        print("---------------------------------------")
        print("SENV commands don't work like regular shell commands (e.g. vim ~/.bashrc).")
        print("When using SENV you can not enter a command and after the command an argument.")
        print("You first have to type your command, in this case v (vim).")
        print("After entering the command a prompt will show up telling you to enter the path/file name.")
        print("---------------------------------------\n")
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")
    
    elif cmd == "li":
        # License Information
        print("Shell Environment Copyright (C) 2025 Zugrăvel Teodor")
        print("This program comes with ABSOLUTELY NO WARRANTY.")
        print("This is free software, and you are welcome to redistribute it under certain conditions.")
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")


    else:
        # Error message
        print(f"{Fore.RED}Please enter a valid command! Enter man to open the manual.{Fore.RESET}")
        input(f"{Fore.GREEN}Press enter to continue . . .{Fore.RESET}")