operation = input("Expression: ").strip()

x,y,z = operation.split(" ")

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case"*":
        print(x*z)
    case"/":
        print(x/z)

