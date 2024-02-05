import emoji


def main():

    emoji_name = input("Input: ")
    try:
        print(f"Output: {emoji.emojize(emoji_name)}")
    except KeyError:
        print("Emoji not found")

if __name__ == "__main__":
    main()
