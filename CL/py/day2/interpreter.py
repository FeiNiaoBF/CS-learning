def mathinter(s):
    x, y, z = s.split(" ")
    x = int(x)
    z = int(z)
    match y:
        case '+':
            return float(x + z)
        case '-':
            return float(x - z)
        case '*':
            return float(x * z)
        case '/':
            return float(x / z)
        case _:
            pass


def main():
    str = input("Expression: ")
    print(mathinter(str))

main()
