amount_due = 50

while amount_due > 0:
    print(f"Amount due {amount_due}")
    money_input = int(input("Insert Coin: "))

    if money_input == 25 or money_input == 10 or money_input == 5:
        amount_due -= money_input

print (f"Change Owed): {abs(amount_due)}")



