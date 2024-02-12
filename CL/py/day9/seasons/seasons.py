from datetime import date
import sys
import inflect

def main():
    birth_date = get_date()
    age = calculate_age_in_minutes(birth_date)
    p = inflect.engine()
    word = p.number_to_words(age, andword="")
    print(f"{word} minutes old")

def get_date():
    birth_date = input("Date of Birth: ")
    birth_date = date.fromisoformat(birth_date)
    if not is_date(birth_date):
        print("Invalid date")
        sys.exit()
    return birth_date

def calculate_age_in_minutes(bdate):
    today = date.today()
    age_minutes = (today - bdate).days * 24 * 60
    return age_minutes

def is_date(bdate):
    today = date.today()
    if type(bdate) is date:
        try:
            if bdate < today:
                return True
        except ValueError:
            return False
    return False



if __name__ == "__main__":
    main()
