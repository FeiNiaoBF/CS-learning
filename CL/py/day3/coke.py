def main():
    # pro_coin = 50
    # print(f"Amount Due: {pro_coin}")
    # coke_coin(pro_coin)
    new_coke_coin()

# def coke_coin(coin):
#     in_coin = int(input("Insert Coin: "))

#     while True:
#         match in_coin:
#             case 5:
#                 coin = coin - in_coin
#                 if coin == 0:
#                     print("Change Owed:", coin)
#                     break
#                 print("Amount Due: ", coin)
#                 in_coin = int(input("Insert Coin: "))
#             case 10:
#                 coin = coin - in_coin
#                 if coin == 0:
#                     print("Change Owed:", coin)
#                     break
#                 print("Amount Due: ", coin)
#                 in_coin = int(input("Insert Coin: "))
#             case 25:
#                 coin = coin - in_coin
#                 if coin == 0:
#                     print("Change Owed:", coin)
#                     break
#                 print("Amount Due: ", coin)
#                 in_coin = int(input("Insert Coin: "))
#             case _:
#                 in_coin = int(input("Insert Coin: "))


def new_coke_coin():
    amount_due = 50
    print(f"Amount Due: {amount_due}")

    while amount_due > 0:
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            amount_due -= coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")

    if amount_due <= 0:
        change_owed = abs(amount_due)
        print(f"Change Owed: {change_owed}")



if __name__ == "__main__":
    main()
