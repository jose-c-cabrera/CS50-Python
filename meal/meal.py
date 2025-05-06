def main():
    actualTime = input("What time is it? ")
    convert(actualTime)
    if >= 7 actualTime <8


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()
