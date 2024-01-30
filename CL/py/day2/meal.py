def main():
    t = input("What time is it?(es: #:## a.m. or ##:## p.m.) ")
    time = convert(t)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):
    t, type = time.split(" ")
    h, m = t.split(":")
    h = float(h)
    m = float(float(m)/60)
    if type == "a.m.":
        return (h + m)
    elif type == "p.m.":
        return (h + 12 + m)
    else:
        return (h + m)


if __name__ == "__main__":
    main()
