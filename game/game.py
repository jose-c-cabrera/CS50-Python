import random


while True:
    try:
        level = input("Level: ")
        number = int(level)
        guess = random.randint(1, number)
        break
    except:
        ValueError



