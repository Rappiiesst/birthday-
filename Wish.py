#!/usr/bin/env python3
# birthday_wish.py
# Termux friendly birthday wish (no external libraries)

import sys
import time
import os

# ANSI color helpers
RESET = "\033[0m"
BOLD = "\033[1m"
COLS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

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

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def type_print(text, delay=0.01):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def big_banner(name):
    # Simple big text made from characters (no figlet)
    line = f"{BOLD}{COLS['magenta']}╔════════════════════════════════╗{RESET}"
    print(line)
    title = f"{BOLD}{COLS['cyan']}   ★ Happy Birthday, {name}! ★   {RESET}"
    print(title)
    print(line)

def animate_balloons(name, rounds=6):
    colors = ["red","yellow","green","cyan","blue","magenta"]
    for r in range(rounds):
        clear()
        col = COLS[colors[r % len(colors)]]
        for i, l in enumerate(BALLOON):
            # shift balloons horizontally for simple animation
            pad = ' ' * ((r + i) % 8)
            print(pad + col + l + RESET)
        print()
        big_banner(name)
        time.sleep(0.6)

def show_cake():
    print()
    for line in CAKE:
        print(COLS['yellow'] + line + RESET)
    print()

def confetti(duration=2.0, density=60):
    import random
    t_end = time.time() + duration
    width = 40
    while time.time() < t_end:
        clear()
        for _ in range(8):
            row = ''.join(random.choice(['*','·','✦','✨','❤','★','•',' ']) for _ in range(width))
            print(row)
        time.sleep(0.15)

def main():
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = input("Dost ka naam daalo: ").strip() or "Dost"
    clear()
    type_print(f"{COLS['green']}Preparing special wish for {name}...{RESET}", 0.02)
    time.sleep(0.8)
    animate_balloons(name, rounds=7)
    confetti(1.2)
    clear()
    big_banner(name)
    show_cake()
    type_print(COLS['cyan'] + BOLD + f"🎉 {name}, Janmadin ki dher saari shubhkaamnayein! 🎉" + RESET, 0.01)
    print()
    type_print("Tumhara dost — " + COLS['magenta'] + "🎈 Sent with Termux script" + RESET, 0.01)
    # beep (may work in Termux)
    sys.stdout.write("\a")
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("\nBye!")
