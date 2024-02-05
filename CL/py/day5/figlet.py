from pyfiglet import Figlet
import sys
import random

def main():
    if len(sys.argv) == 1:
        input_str = input("Input: ")
        print_figlet_random(input_str)
    elif len(sys.argv) == 3:
        command = sys.argv[1]
        fonts = sys.argv[2]
        print_figlet_command(command, fonts)
    else:
        # sys.exit("Usage: python3 figlet.py ([command] [font])")
        sys.exit("Invalid usage")


def print_figlet_command(command, fonts):
    try:
        if command == "-f" or command == "--font" and fonts in Figlet().getFonts():
            text = input("Input: ")
            print_figlet_default(text, fonts)
        else:
            sys.exit("Invalid usage")

    except KeyError:
        print("Font not found")


def print_figlet_random(text):
    f = Figlet()
    f.setFont(font=random.choice(f.getFonts()))
    # print(random.choice(f.getFonts()))
    print(f.renderText(text))

def print_figlet_default(text, fonts):
    f = Figlet()
    f.setFont(font=fonts)
    print(f.renderText(text))

if __name__ == "__main__":
    main()
