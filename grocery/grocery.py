grocery = {

}
count = 0
while True:
    try:
        item = input().upper()
        get(item) = grocery

        if item in grocery:
            count += 1

    except EOFError:
        break



