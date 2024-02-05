import inflect

def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass
    print(adieu_name(names))

def adieu_name(names):
    p = inflect.engine()
    return f"Adieu, adieu, to {p.join(names)}"

main()
