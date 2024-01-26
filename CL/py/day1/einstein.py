def emc(m):
    e = m * (int)(pow(300000000, 2))
    return e


def main():
    s = (int)(input("m:  "))
    e = emc(s)
    print("E: ", +e)

main()
