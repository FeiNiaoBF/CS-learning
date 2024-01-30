def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_valid_len(s) and starts_with_two_letters(s) and has_valid_numbers(s) and has_no_punctuation(s):
        return True
    else:
        return False

def is_valid_len(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return s[:2].isalpha()

def has_valid_numbers(s):
    if s[-1].isdigit() and s[-1] != '0':
        return s[:-1].isalpha()
    else:
        return False

def has_no_punctuation(s):
    return s.isalnum()

main()
