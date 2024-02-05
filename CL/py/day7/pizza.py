import csv
import sys
import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        try:
            file_path = sys.argv[1]
            if not file_path.endswith(".csv"):
                sys.exit("Not a CSV file")
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            with open(file_path, "r") as file:
                print(print_pizza_table(file))

def print_pizza_table(file):
    reader = csv.reader(file)
    return f"{tabulate.tabulate(reader, headers='firstrow', tablefmt='grid')}"


if __name__ == "__main__":
    main()
