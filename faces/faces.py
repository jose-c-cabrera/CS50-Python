def main():
    usersInput = input()
    #converted = convert(usersInput)
    print(convert(usersInput))


def convert(to):
   new = to.replace(":(","😐")
   new = new.replace(":)","🙂")
   return new

main()
