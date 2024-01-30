

def main():

    while True:
        date = input("Date: ")
        if not date:
            print("Please enter a valid date.")
            continue
        try:
            print(date_format(date))
            break
        except ValueError as e:
            print(e)
            continue


def date_format(date):
    months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}
    date = date.replace(", ", "/").replace(" ", "/")
    m, d, y = date.split("/")
    if m.isdigit():
        m = int(m)
    else:
        m = months.get(m)
        if m is None:
            raise ValueError("Invalid month")
    if d.isdigit():
        d = int(d)
        if d < 1 or d > 31:
            raise ValueError("Invalid day")
    else:
        raise ValueError("Invalid day")

    return f"{y}-{int(m):02}-{int(d):02}"



if __name__ == "__main__":
    main()
