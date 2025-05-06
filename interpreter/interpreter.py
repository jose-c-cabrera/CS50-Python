operation = input("Expression: ").strip()

x,y,z = operation.split(" ")

match y:
    case "+":
        print(float(int(x)+int(z)))
    case "-":
        print(float(int(x)-int(z)))
    case"*":
        print(float(int(x)*int(z)))
    case"/":
        print(float(int(x)/int(z)))

