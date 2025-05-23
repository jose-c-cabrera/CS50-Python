import inflect

p = inflect.engine()
names = []

try:
    while True:
        name_input = input("Name: ")
        names.append(name_input)
except EOFError:
    print()
    print("Adieu, adieu, to " p.join(names))

