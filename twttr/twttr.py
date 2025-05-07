def main ():
    user_input = input("Input: ")
    remove_vowels(user_input)

def remove_vowels(string):
    for char in string:
        if char == 'a' or char =='e' or char== 'i' or char == 'o' or char == 'u':
            string -= char
            print (string)
main()
