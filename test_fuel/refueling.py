
def main():


def convert(fraction):

while True:
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split(sep='/')
        x = int(x)
        y = int(y)
        if x > y:
            continue
        percentage = round((x/y)*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

def gauge(percentage):

    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
