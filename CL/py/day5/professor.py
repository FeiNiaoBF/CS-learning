
import random


def main():
    score = 0
    times = 10
    level =  get_level("Level: ")
    for _ in range(times):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        miss = 0
        while miss < 3:
            try:
                in_ans = int(input(f"{x} + {y} = "))
                if in_ans == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    miss += 1
            except ValueError:
                print("EEE")
                continue
        if miss == 3:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level")
    else:
        return random.randint((10 ** (level-1)), (10 ** level) - 1)


if __name__ == "__main__":
    main()
