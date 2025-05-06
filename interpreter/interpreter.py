operation = input("Expression: ").strip()

x,y,z = operation.split(" ")

match y:
    case "+":
        print(float(x+z))
    case "-":
        print(float(x-z))
    case"*":
        print(float(x*z))
    case"/":
        print(float(x/z))

