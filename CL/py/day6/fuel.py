def main():
    while True:
        try:
            s = input("Fraction: ")
        except ValueError:
            print("Please enter a number.")
        else:
            print(gauge(convert(s)))
            break


def convert(fraction):
    try:
        x, y = fraction.split("/")
        return int(x) / int(y)
    except (ZeroDivisionError, ValueError):
        return "Invalid input!"


def gauge(percentage):
    try:
        x = int(percentage)
        if x >= 99:
            return 'F'
        elif x <= 1:
            return 'E'
        else:
            return str(x) + '%'
    except ValueError:
        return "Invalid input!"

if __name__ == "__main__":
    main()
