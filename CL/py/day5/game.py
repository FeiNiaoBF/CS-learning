import random

def main():
    guess_game()

def guess_game():
    level = get_valid("Level: ")
    number = random.randint(1, level)

    while True:
        guess = get_valid("Guess: ")
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_valid(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            continue

if __name__ == "__main__":
    main()
