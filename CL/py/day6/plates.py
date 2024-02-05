def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    first_two = s[:2]
    to_end = s[2:]
    if not first_two.isalpha() or not to_end.isalnum():
        return False
    if not to_end.isnumeric() and not to_end.isalpha():
        return False
    if to_end[0] == '0':
        return False
    return True

if __name__ == "__main__":
    main()
''
