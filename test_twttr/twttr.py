def main():

def shorten(word):
    word = input("Input: ")
    print(remove_vowels(word))

def remove_vowels(string):
    twitter_word = ""

    for char in string:
        if char == 'a' or char =='e' or char== 'i' or char == 'o' or char == 'u'or char == 'A' or char =='E' or char== 'I' or char == 'O' or char == 'U':
            continue
        else:
            twitter_word+=char
    return (twitter_word)

if __name__ == "__main__":
    main()
