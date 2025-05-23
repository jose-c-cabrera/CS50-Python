import inflect

names = []

while (True):
    try:
        name_input = input("Name: ")
        names.append(name_input)

        p.join(names)

    except:
        (ValueError, IndexError):
        continue

