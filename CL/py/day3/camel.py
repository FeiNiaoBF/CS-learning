def main():
    name = input("camelCase: ")

    print("snake_case: ", end='')
    snake_case_name(name)

def snake_case_name(name):
    for c in range(len(name)):
        if name[c].isupper():
            print('_', end='')
            print(name[c].lower(), end='')
        else:
            print(name[c], end='')
    print()

if __name__ == "__main__":
    main()
