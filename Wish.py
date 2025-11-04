#!/usr/bin/env python3
# Infinite Birthday Wisher by Rohit
# Works perfectly in Termux (no extra modules)

import os, sys, time, random

# --- Colors ---
RESET = "\033[0m"
BOLD = "\033[1m"
COLS = {
    "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
    "blue": "\033[34m", "magenta": "\033[35m", "cyan": "\033[36m"
}

# --- Balloons ASCII ---
BALLOON = [
    "     .-''''-.",
    "   .'  .--.  '.",
    "  /  .'    '.  \\",
    " :  /        \\  :",
    " | |  HAPPY   | |",
    " : |  BIRTH-  | :",
    "  \\ \\  DAY!  / /",
    "   '.`'----'`.'",
    "     '-.  .-'",
    "        ||",
    "        ||",
    "        ||",
    "       /  \\"
]

# --- Cake ASCII ---
CAKE = [
    "        ,,,,,",
    "       |||||",
    "     __|||||__",
    "    |  ~~~~~  |",
    "  __|  HAPPY  |__",
    " |  |  BIRTH  |  |",
    " |  |   DAY!  |  |",
    " |__|_________|__|"
]

# --- Birthday wishes list ---
WISHES = [
    "🎉 May your day be full of smiles and sunshine!",
    "🎂 Wishing you endless happiness and success!",
    "🎈 May all your dreams come true this year!",
    "💫 Stay blessed, healthy and always amazing!",
    "🌟 Another year older, wiser and happier!",
    "❤️ Sending loads of love and laughter your way!",
    "💐 Hope your life sparkles like your smile!",
    "🔥 Keep shining, keep rocking — it’s your day!",
    "🎁 May your future be as bright as candles on your cake!",
    "☀️ You deserve every bit of joy in the world!",
    "🌈 Stay positive, stay awesome — always!",
]

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def type_print(text, delay=0.01):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def confetti(duration=1.5):
    t_end = time.time() + duration
    while time.time() < t_end:
        row = ''.join(random.choice(['*','✨','❤','★','·','+',' ']) for _ in range(40))
        print(random.choice(list(COLS.values())) + row + RESET)
        time.sleep(0.1)

def show_banner(name):
    print(f"{BOLD}{COLS['cyan']}╔═══════════════════════════════════╗{RESET}")
    print(f"{BOLD}{COLS['magenta']}   ★★ Happy Birthday, {name}! ★★   {RESET}")
    print(f"{BOLD}{COLS['cyan']}╚═══════════════════════════════════╝{RESET}")

def show_balloons(name):
    color = random.choice(list(COLS.values()))
    for l in BALLOON:
        print(color + l + RESET)
    print()
    show_banner(name)

def show_cake():
    for line in CAKE:
        print(COLS['yellow'] + line + RESET)
    print()

def main():
    name = input("Apne dost ka naam likho: ").strip() or "Dost"
    clear()
    type_print(f"{COLS['green']}🎉 Special birthday wish loading for {name}...{RESET}", 0.02)
    time.sleep(1)

    # Infinite loop of blessings
    while True:
        clear()
        show_balloons(name)
        show_cake()
        wish = random.choice(WISHES)
        print()
        type_print(random.choice(list(COLS.values())) + BOLD + wish + RESET, 0.01)
        print()
        confetti()
        time.sleep(1)
        # Add more wishes dynamically (infinite feel)
        extra = f"✨ {name}, stay happy and keep smiling always! ✨"
        WISHES.append(extra)
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print(f"{COLS['yellow']}Program stopped. Have a wonderful day!{RESET}")
