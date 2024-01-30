def main():
    while True:
        try:
            s = input("Fraction: ")
        except ValueError:
            print("Please enter a number.")
        else:
            print(fuel_gauge(s))
            break


def fuel_gauge(fuel):
    try:
        x, y = fuel.split("/")
        z = int(int(x) / int(y) * 100)
        if z >= 100:
            return 'F'
        elif z <= 0:
            return 'E'
        else:
            return str(z) + '%'
    except (ValueError, ZeroDivisionError):
        return "Invalid input!"


if __name__ == "__main__":
    main()
