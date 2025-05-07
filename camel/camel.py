def main ():
    camelCase = input("camelCase: ").strip()
    print(to_snake_case(camelCase))


def to_snake_case(camel_string):
    snake_string = ""
    for char in camel_string:
        if char.isupper():
            snake_string += "_" +char.lower()
        else:
            snake_string += char
    return snake_string

main()
