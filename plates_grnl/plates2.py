def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else: print("Invalid")

def is_valid(platep):

    if not platep.isalnum():
        return False

    if len(platep) < 2 or len(platep) > 6:
        return False

    if platep[:2].isdigit():
        return False

    for char in platep:
        if char.isdigit():
            if char == "0":
                return False
        break

    return True

main()


