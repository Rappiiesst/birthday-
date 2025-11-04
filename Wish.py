os.system("play happy.mp3 &")
import os, time, random
from colorama import Fore, Style

# Safe looping (press Ctrl+C to stop)
name = input(Fore.CYAN + "🎂 Enter your friend's name: " + Style.RESET_ALL)

ascii_arts = [
r"""
  🎂🎉 HAPPY BIRTHDAY 🎉🎂
      ________
     |~ ~ ~ ~|
     |  HBD  |
     |_______|
""",
r"""
  🎈🎈🎈🎈🎈
  ╔══╗──────╔╗
  ║╚═╬══╦══╬╬╦═╗
  ║╔╗║╔╗║╔═╣║║╔╝
  ║╚╝║╚╝║╚═╣║║║
  ╚══╩══╩══╩╩╩╝
  💖 Happy Birthday 💖
""",
r"""
  🎉🍰🎂✨
   *~*~*~*~*~*
     HAPPY
     BIRTHDAY
     TO YOU 💝
   *~*~*~*~*~*
"""
]

wishes = [
    f"🎊 {name}, tumhara har din khushiyon se bhara rahe!",
    f"🎂 Happy Birthday {name}! Life tumhari cake jaisi sweet ho! 🍰",
    f"💐 Bhagwan tumhe sehat, sukh aur safalta de! 🌟",
    f"🎁 Tumhe mile duniya bhar ki khushiyan aur pyaar ❤️",
    f"🌈 {name}, tum hamesha muskurate raho aur sabko khush rakho!"
]

colors = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.RED]

def rainbow_text(text):
    shades = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
    result = ""
    for i, ch in enumerate(text):
        result += shades[i % len(shades)] + ch
    return result + Style.RESET_ALL

try:
    while True:
        os.system("clear")
        color = random.choice(colors)
        art = random.choice(ascii_arts)
        wish = random.choice(wishes)

        print(rainbow_text(art))
        print(rainbow_text(wish))
        print(color + "🎉🎈🎂 " + " ".join(random.choices(["💖","🎊","🎁","🎉","🎈","✨"], k=25)) + Style.RESET_ALL)
        time.sleep(2)
except KeyboardInterrupt:
    print(Style.RESET_ALL + "\n🎂 Celebration ended safely. Happy Birthday once again!")
