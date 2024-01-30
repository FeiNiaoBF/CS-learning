
grocery = {}

def main():
    while True:
        try:
            itme = input("").upper()
            if itme == "":
                break
            else:
                add_item(itme)
        except EOFError:
            print_list()
            break
    return

def add_item(item):
    if item in grocery:
        grocery[item] += 1
    else:
        grocery.update({item: 1})

def print_list():
    for item in grocery:
        print(f"{grocery[item]} {item}")

if __name__ == "__main__":
    main()
