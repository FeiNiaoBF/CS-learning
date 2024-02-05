import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            name_file = sys.argv[1]
            out_file = sys.argv[2]
            if not name_file.endswith(".csv") and not out_file.endswith(".csv"):
                sys.exit("Not a CSV file")
            data_to_csv = read_csv(name_file)
            write_csv(out_file, cut_name(data_to_csv))

        except FileNotFoundError:
            sys.exit(f"Could not read {name_file}")

def write_csv(out_file, data):
    try:
        with open(out_file, 'w', newline='') as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for row in data:
                writer.writerow({"first": row[0], "last": row[1], "house": row[2]})

    except FileNotFoundError:
        sys.exit(f"Could not write {out_file}")



def read_csv(in_file):
    try:
        with open(in_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        sys.exit(f"Could not read {in_file}")

def cut_name(names):
    out_names = [['first', 'last', 'house']]
    for row in names:
        name, house = row["name"], row["house"]
        first, last = map(str.strip, name.split(", "))
        out_names.append([first, last, house])
    return out_names


if __name__ == "__main__":
    main()
