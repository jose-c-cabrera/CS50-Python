operation = input("Expression: ").strip()

x,y,z = operation.split(" ")

match y:
    case "+":
        print(round(float(int(x)+int(z)),1))
    case "-":
        print(round(float(int(x)-int(z)),1))
    case"*":
        print(round(float(int(x)*int(z)),1))
    case"/":
        print(round(float(int(x)/int(z)),1))

