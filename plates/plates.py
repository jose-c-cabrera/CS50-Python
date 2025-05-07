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
    for char in proposition:
        if char.count() > 6 or char.count()<2:
            return False
