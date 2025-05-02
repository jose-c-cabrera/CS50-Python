def main():
    usersInput = input()
    converted = convert(usersInput)
    print(converted)


def convert(to):
   new = to.replace(":(","😐")
   new = new.replace(":)","🙂")
   return new

main()

