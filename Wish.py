import os
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# 💖 Fixed name
name = "Anushi 💋"
lover = "Rohit ❤️"

# 🎵 Optional background song
if os.path.exists("happy.mp3"):
    os.system("play happy.mp3 &")

# 🎨 Colors
colors = [Fore.RED, Fore.MAGENTA, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.GREEN]

# 🎂 Cakes
cakes = [
r"""
        i i i i i i
       |:H:a:p:p:y:|
     __|___________|__
    |^^^^^^^^^^^^^^^^^|
    |:B:i:r:t:h:d:a:y:|
    |                 |
    ~~~~~~~~~~~~~~~~~~~
""",
r"""
   🎂🎂🎂🎂🎂
  🎉 HAPPY 🎉
 🎈 BIRTHDAY 🎈
   🎂🎂🎂🎂🎂
""",
r"""
   🎊🎂  H A P P Y  🎂🎊
  💖  B I R T H D A Y  💖
   🎈🎂   A N U S H I   🎂🎈
"""
]

# 🎁 Wishes
wishes = [
    "🎂 Rohit ki Jaan Anushi 💋, tumhara din pyar aur khushiyon se bhara rahe!",
    "💖 Tumhari muskurahat duniya roshan karti hai 🌟",
    "🎈 Tum jiyo hazaron saal, yehi dua hai Rohit ki 💞",
    "🎉 Har saal tum aur bhi beautiful lagti ho 😘",
    "🎁 Tumhari life chocolate cake jaise meethi rahe 🍫",
    "🌈 Rohit tumhe hamesha khush dekhna chahta hai 💘",
    "🎊 Happy Birthday once again Anushi 💋, stay happy forever 💫",
]

# 💞 Love Shayari
shayari = [
    "💌 Tum meri zindagi ka woh hissa ho, jahan har subah sirf tumse shuru hoti hai ❤️",
    "💖 Har saans mein tera naam hai, har dhadkan mein tera ehsaas hai 💋",
    "🌙 Tum meri duaon ka woh hissa ho jo har raat maangta hoon ⭐",
    "💘 Tum ho toh lagta hai har pal meetha hai, har lamha khubsurat hai 💫",
    "🌹 Ishq woh nahi jo zuban se kaha jaaye, ishq toh woh hai jo aankhon se samjha jaaye 💞",
    "🎶 Tum meri muskurahat ho, meri har khushi ka sabab ho 💓",
    "❤️ Rohit ka pyaar Anushi ke liye kabhi kam nahi hoga 💋",
]

# 🌈 Rainbow text effect
def rainbow(text):
    shades = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return "".join(shades[i % len(shades)] + ch for i, ch in enumerate(text)) + Style.RESET_ALL

# 🎊 Emoji rain animation
def emoji_rain():
    emojis = ["🎂", "🎉", "🎈", "💖", "💋", "🎊", "🌸", "🥳", "🍰", "💕"]
    print(random.choice(colors) + "".join(random.choice(emojis) for _ in range(60)))

# 🔁 Infinite celebration
try:
    while True:
        os.system("clear")
        emoji_rain()
        print(rainbow(f"\n★🎂 Happy Birthday, {name}! 🎂★\n"))
        print(random.choice(colors) + random.choice(cakes))
        print(rainbow(random.choice(wishes)))
        print(random.choice(colors) + "\n" + random.choice(shayari))
        print(random.choice(colors) + f"\n💌 Tumhara {lover} — Forever Yours 💋")
        emoji_rain()
        print(Fore.WHITE + "\n(Press Ctrl + C to stop celebration)\n")
        time.sleep(3)
except KeyboardInterrupt:
    os.system("clear")
    print(Fore.MAGENTA + "\n🎉 Celebration stopped manually. Rohit ❤️ always loves Anushi 💋 forever 🎂")
