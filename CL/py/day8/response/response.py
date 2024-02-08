import validator_collection
import validators

def main():
    print(parse(input("What's your email address? ")))

def parse(s):
    email = s.strip()
    if is_valid_email(email):
        return "Valid"
    else:
        return "Invalid"

def is_valid_email(email):
    return validators.email(email) and validator_collection.is_email(email)

if __name__ == "__main__":
    main()
    