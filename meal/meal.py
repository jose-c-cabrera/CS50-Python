def main():
    actualTime = input("What time is it? ")
    convert(actualTime)
    if actualTime >= 7 and < 8:
        print("breakfast time")
    elif actualTime >=12 and < 13:
        print("lunch time")
    elif actualTime >=18 and < 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()
