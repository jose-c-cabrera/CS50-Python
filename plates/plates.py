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

    if not proposition.isalnum():
        return False

    for char in set(proposition):
        count = proposition.count(char)
        if count > 6 or count < 2:
            return False

    if proposition[0:2].isdigit():
        return False

    return True

