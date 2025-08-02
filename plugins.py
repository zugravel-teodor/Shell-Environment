# To add a plugin, copy the plugin_name() to your senv.py exactly where you want it to appear.

import os
from datetime import datetime
import random
import getpass
import time
from colorama import Fore, init
import subprocess

# Boot animation ----------------------------------------

# Code:

def boot_anim():
    time.sleep(0.5)
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] python is running")
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] from colorama: importing Fore")
    time.sleep(2)
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] importing os")
    time.sleep(0.3)
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] importing datetime")
    time.sleep(0.5)
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] importing time")
    time.sleep(1)
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] importing random")
    time.sleep(0.5)
    print(f"[ {Fore.GREEN} ok {Fore.RESET} ] booting system")
    time.sleep(0.7)
    os.system("clear")

# Run:

# boot_anim()

# Random quotes ------------------------------------------

# Code:

def Quote():
    quotes = [
    "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie",
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "The most important thing is to be able to think for yourself. - Richard Stallman",
    "You can't just sit there and wait for someone to give you a job. You have to go out and create your own opportunities. - Terry Davis",
    "Software is like sex: it's better when it's free. - Linus Torvalds",
    "The best way to predict the future is to invent it. - Alan Kay",
    "In programming, the hard part isn't solving problems, but deciding what problems to solve. - Paul Graham",
    "Simplicity is the soul of efficiency. - Austin Freeman",
    "The most damaging phrase in the language is: 'We've always done it this way.' - Grace Hopper",
    "If you think your users are idiots, only idiots will use it. - Linus Torvalds",
    "The best code is no code at all. - Jeff Atwood",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Programming is not about what you know; it's about what you can figure out. - Chris Pine",
    "There are only two kinds of programming languages: those people always bitch about and those nobody uses. - Bjarne Stroustrup",
    "The most effective debugging tool is still careful thought, coupled with judiciously placed print statements. - Linus Torvalds",
    "Nothing focuses the mind better than the constant sight of a competitor who wants to wipe you off the map. - Wayne Calloway",
    "A good programmer is someone who always looks both ways before crossing a one-way street. - Doug Linder",
    "The best way to get a project done faster is to start sooner. - Jim Highsmith",
    "The key to successful programming is to keep it simple. - Richard Stallman",
    "The only thing that matters is that you get the job done. - Terry Davis",
    "Programming is the art of algorithm design and the craft of debugging errant code. - Ellen Ullman",
    "The greatest danger in times of turbulence is not the turbulence; it is to act with yesterday's logic. - Peter Drucker",
    "Good programmers know what to write. Great programmers know what to rewrite. - Anonymous",
    "The best part of programming is the opportunity to learn something new every day. - Linus Torvalds",
    "Code is like humor. When you have to explain it, it’s bad. - Cory House",
    "The only way to go fast is to go well. - Robert C. Martin",
    "You can't have great software without a great team, and most software teams behave like dysfunctional families. - Jim McCarthy",
    "The best code is the code you don't have to write. - Linus Torvalds",
    "The future of programming is not about code, it's about people. - Richard Stallman",
    "If you can't explain it simply, you don't understand it well enough. - Albert Einstein",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Programming, like poetry, is a creative act. - Terry Davis"
]


    quote = random.choice(quotes)
    print(quote)





# Run:

# Quote()


# Custom plugin --------------------------------------------

# Code:

def custom_plugin():
    print("Hello, world!")

# Run:

# custom_plugin()




