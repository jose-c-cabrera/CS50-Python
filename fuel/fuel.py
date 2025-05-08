while True:
    try:
        users_input = input("Fraction: ")
        x,y = users_input.split(sep='/')
        fraction = round((int(x)/int(y))*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
percentage = f"{fraction}%"
if percentage > 1 and percentage < 99:
    print(percentage)
elif percentage < 1:
    print("E")
else:
    print("F")



