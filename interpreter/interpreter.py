operation = input("Expression: ").strip()

x,y,z = operation.split(" ")

match y:
    case "+":
        print(round(float(int(x)+int(z))),2)
    case "-":
        print(round(float(int(x)-int(z))),2)
    case"*":
        print(round(float(int(x)*int(z))),2)
    case"/":
        print(round(float(int(x)/int(z))),2)

