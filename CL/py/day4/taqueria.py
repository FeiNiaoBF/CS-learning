menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


def main():
    price = 0.0
    while True:
        try:
            itme = input("Item:").lower()
            if is_menu(itme):
                price = total(itme, price)
                print(f"Total: ${price:.2f}")
            else:
                continue
        except EOFError:
            break
    return


def is_menu(itme):
    return itme in menu

def total(itme, price):
    price += menu[itme]
    return price

if __name__ == "__main__":
    main()
