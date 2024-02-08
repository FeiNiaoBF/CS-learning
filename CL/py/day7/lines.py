import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        try:
            file_path = sys.argv[1]
            if not file_path.endswith(".py"):
                sys.exit("Not a Python file")
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            with open(file_path, "r",encoding='utf-8') as file:
                print(get_line_number(file))

def get_line_number(file_path):
    line_num = 0
    for line in file_path:
        if line.rstrip().startswith("#") or line.rstrip() == "" or line.rstrip().startswith(" #"):
            continue
        if line.rstrip().startswith('\n'):
            continue
        else:
            line_num += 1

    return line_num

if __name__ == "__main__":
    main()
