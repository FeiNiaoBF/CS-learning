def main():
    s = playback()
    print(s, sep="...")

def playback():
    str_input = input("")
    return str_input.replace(' ', '...')

main()
