def main():
    actualTime = input("What time is it? ")
    timeInHours = convert(actualTime)

    if 7 <= timeInHours < 8:
        print("breakfast time")
    elif 12 <= timeInHours < 13:
        print("lunch time")
    elif 18 <= timeInHours < 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()
