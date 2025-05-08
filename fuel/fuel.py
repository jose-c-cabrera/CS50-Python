while True:
    input = input("Fraction: ")
    x,y = input.split(sep='/')
    fraction = round((int(x)/int(y))*100)
    percentage = f"{fraction}%"

    print(percentage)



