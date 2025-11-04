import os
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# 🎈 User se naam lena
name = input(Fore.CYAN + "🎂 Enter your friend's name: " + Style.RESET_ALL)

# 🎶 Optional: agar background music play karna hai (Termux me play command installed ho)
if os.path.exists("happy.mp3"):
    os.system("play happy.mp3 &")

# 🎨 Color list
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# 🎂 Cake design aur wishes
cake_art = r"""
        i i i i i i
       |:H:a:p:p:y:|
     __|___________|__
    |^^^^^^^^^^^^^^^^^|
    |:B:i:r:t:h:d:a:y:|
    |                 |
    ~~~~~~~~~~~~~~~~~~~
"""

wishes = [
    "🎉 Tumhara din khushiyon se bhara rahe!",
    "🎂 Bhagwan kare tumhe har khushi mile jo tum chaaho!",
    "🎁 Tumhari life sweet ho jaise cake ka frosting 🍰",
    "💫 Tum hamesha muskurate raho aur duniya roshan karo 🌟",
    "💖 Tumhara har sapna poora ho! ✨",
    "🎈 Happy Birthday once again! Party hard! 🎊",
]

# 🌈 Rainbow text effect
def rainbow(text):
    shades = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    result = ""
    for i, ch in enumerate(text):
        result += shades[i % len(shades)] + ch
    return result + Style.RESET_ALL

# 🔁 Infinite loop (manual stop with Ctrl + C)
try:
    while True:
        os.system("clear")
        print(rainbow(f"★🎂 Happy Birthday, {name}! 🎂★\n"))
        print(random.choice(colors) + cake_art)
        print(rainbow(random.choice(wishes)))
        print(random.choice(colors) + f"\n💌 Tumhara dost — Rohit ❤️")
        print(Fore.WHITE + "\n(Press Ctrl + C to stop celebration)\n")
        time.sleep(2)
except KeyboardInterrupt:
    print(Fore.CYAN + "\n🎉 Celebration stopped manually. Happy Birthday again! 🎂")
