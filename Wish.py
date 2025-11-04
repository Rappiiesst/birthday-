import os, sys, time, random

# Ensure emoji/text show correctly in Termux
os.system("clear")
sys.stdout.reconfigure(encoding='utf-8')

# Play background birthday song
os.system("play happy.mp3 &")

# 🎉 Banner
banner = """
🎉🎂  H  A  P  P  Y  🎂🎉
💖  B  I  R  T  H  D  A  Y  💖
🎈     A N U S H I     🎈
"""

print(banner)
time.sleep(1)

# 🎁 Birthday Wishes
wishes = [
    "🎂 Rohit ki Jaan Anushi 💋, tumhara din pyar aur khushiyon se bhara rahe!",
    "💖 Tumhari muskurahat duniya roshan karti hai 🌟",
    "🎈 Tum jiyo hazaron saal, yehi dua hai Rohit ki 💞",
    "🎉 Har saal tum aur bhi beautiful lagti ho 😘",
    "🎁 Tumhari life chocolate cake jaise meethi rahe 🍫",
    "🌈 Rohit tumhe hamesha khush dekhna chahta hai 💘",
    "🎇 Happy Birthday once again Anushi 💋, stay happy forever 💫"
]

# 💞 Love Shayari
shayari = [
    "💌 Tum meri zindagi ka woh hissa ho, jahan har subah sirf tumse shuru hoti hai ❤️",
    "💖 Har saans mein tera naam hai, har dhadkan mein tera ehsaas hai 💋",
    "🌙 Tum meri duaon ka woh hissa ho, jo har raat maangta hoon ⭐",
    "💞 Tum ho toh lagta hai har pal pyara hai, warna sab kuch bekar sa hai 💔",
    "💘 Tere bina adhuri si lagti hai zindagi, jaise geet bina sargam 💫"
]

# ♾️ Infinite Loop (never ends)
while True:
    os.system("clear")
    print(banner)
    print("💖  Rohit se Anushi ke liye Special Birthday Wishes 💖\n")
    
    for wish in wishes:
        for ch in wish:
            print(ch, end='', flush=True)
            time.sleep(0.03)
        print("\n")
        time.sleep(1)

    print("\n🌹  Ishq Bhari Shayari 🌹\n")
    for line in shayari:
        for ch in line:
            print(ch, end='', flush=True)
            time.sleep(0.03)
        print("\n")
        time.sleep(1.5)

    print("✨ — From Rohit with Endless Love 💖 — ✨\n")
    time.sleep(3)
