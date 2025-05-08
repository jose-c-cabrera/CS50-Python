while True:
    try:
        input = input("Fraction: ")
        x,y = input.split(sep='/')
        fraction = round((int(x)/int(y))*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
percentage = f"{fraction}%"
print(percentage)



