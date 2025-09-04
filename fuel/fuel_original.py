while True:
    try:
        users_input = input("Fraction: ")
        x,y = users_input.split(sep='/')
        x = int(x)
        y = int(y)
        if x > y:
            continue
        percentage = round((x/y)*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")


