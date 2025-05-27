import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

secret = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1 or guess > level:
            continue
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass



