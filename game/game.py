import random
guess = random.randint()

while True:
    try:
        level = input("Level: ")
        number = int(level)
        break
    except:
        ValueError


