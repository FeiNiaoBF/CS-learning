def main():
    word = input("input: ")
    result = shorten_words(word)
    print(f"Output: {result}")

def shorten_words(word):
    vowels = "aeiouAEIOU"
    for c in word:
        if c in vowels:
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()
