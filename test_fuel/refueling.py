
def main():
    while True:
        try:
            fraction_input = input("Fraction: ")
            percentage = convert(fraction_input)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))



def convert(fraction):

    x,y = fraction.split(sep='/')
    x = int(x)
    y = int(y)

     if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator.")

    percentage = round((x / y) * 100)
    return percentage

def gauge(percentage):

    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
