'''
In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”),
output $20. Otherwise, output $100. Ignore any leading whitespace in the user`s greeting,
and treat the user`s greeting case-insensitively.
'''

def bank():
    input_str = input("Greeting: ")
    if input_str.find("Hello") == 0:
        return "$0"
    elif input_str.find("H") == 0:
        return "$20"
    elif input_str.find("h") == 0:
        return "$20"
    else:
        return "$100"


def main():
    ret = bank()
    print(ret)

main()
