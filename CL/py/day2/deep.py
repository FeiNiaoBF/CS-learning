def answer():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if x == "42" or x == "Forty Two" or x == "forty-two":
        return True
    else:
        return False

def main():
    if answer():
        print('Yes')
    else:
        print('No')

main()
