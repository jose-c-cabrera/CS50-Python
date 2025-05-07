def main ():
    camelCase = input("camelCase: ").strip()
    to_snake_case(camelCase)


def to_snake_case(camel_string):
    snake_string = ""
    for char in camel_string:
        if(char.isupper()):
            snake_string += "_" +char.lower()
        else:
            snake_str += char
    return snake_string

main()
