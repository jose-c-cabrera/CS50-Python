def main():
    greeting = input("Greeting: ").strip()
    print(value(greeting))

def value(greeting):

    if greeting.startswith("Hello"):
        return(int(0))
    elif greeting.startswith("hello"):
        return(int(0))
    elif greeting.startswith("H"):
        return(int(20))
    elif greeting.startswith("h"):
        return(int(20))
    else:
        return(int(100))

if __name__ == "__main__":
    main()

