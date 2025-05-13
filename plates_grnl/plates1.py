#Must start with two letters
#Max 6 characters - Min 2 characters
#Numbers at the end
#First number cannot be a 0
#No periods, spaces, punctuaion marks allowed

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(proposition):

    if len(proposition) < 2 or len(proposition) > 6:
        return False

    if not proposition[0:2].isalpha():
        return False

    if not proposition.isalnum():
        return False

    for i in range(len(proposition)):
        if proposition[i].isdigit():
            if proposition[i] == '0':
                return False
            if not proposition[i:].isdigit():
                return False
            break

    return True

main ()


