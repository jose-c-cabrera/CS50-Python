import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            random_number = random.randint(1, level)
            break
    except ValueError:
        pass




