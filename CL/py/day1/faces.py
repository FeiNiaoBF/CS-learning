def makFaces(in_s):
    out_s = in_s.replace(":)", "🙂").replace(":(", "🙁")
    return out_s



def main():
    s = input("")
    out_str = makFaces(s)
    print(out_str)

main()

