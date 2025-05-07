amount_due = 50

while amount_due > 0:
    print(f"Amount due {amount_due}")
    money_input = int(input("Insert Coin: "))

    if money_input == 25:
        amount_due -= money_input
    elif money_input == 10:
        amount_due -= money_input
    elif money_input == 5:
        amount_due -= money_input


