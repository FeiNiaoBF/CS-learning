def main():
    word = input("input: ")
    result = shorten(word)
    print(f"Output: {result}")



def shorten(word):
    vowels = "aeiouAEIOU"
    for c in word:
        if c in vowels:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()
