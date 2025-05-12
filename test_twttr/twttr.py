
def main():
    string = input("Input: ")
    print(shorten(string))

def shorten(word):
    twitter_word = ""

    for char in word:
        if char == 'a' or char =='e' or char== 'i' or char == 'o' or char == 'u'or char == 'A' or char =='E' or char== 'I' or char == 'O' or char == 'U':
            continue
        else:
            twitter_word+=char
    return print(twitter_word)

if __name__ == "__main__":
    main()
