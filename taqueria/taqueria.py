menu = {
    "name": "Baja Taco", "price" : 4.25,
    "name": "Burrito", "price" : 7.50,
    "name": "Bowl", "price" : 8.50,
    "name": "Nachos", "price" : 11.00,
    "name": "Quesadilla", "price" : 8.50,
    "name": "Super Burrito", "price" : 8.50,
    "name": "Super Quesadilla", "price" : 9.50,
    "name": "Taco", "price" : 3.00,
    "name": "Tortilla Salad", "price" : 8.00
}

while True:
    item = input("Item: ").title()
    print(f"Total: $ {menu["price"]}")


