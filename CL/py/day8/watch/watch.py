import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s.strip()
    if matches := re.search(r"\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"", s, re.IGNORECASE):
        ret = matches.group(1)

        return "https://youtu.be/" + ret

    return None



if __name__ == "__main__":
    main()
