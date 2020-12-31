import string
def pangram(phrase):
    b = list(string.ascii_lowercase)
    ph = True
    for i in b:
        if i in phrase.lower():
            pass
        else:
            ph = False
    if ph == True:
        print("yes, the phrase is pangram")
    else:
        print("no, the phrase is not pangram")

phrase = input("Enter the string that you think is pangram\n")
pangram(phrase)