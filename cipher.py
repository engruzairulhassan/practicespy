import string
def cipher(str, choice):
    import string
    values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    keys =   ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    dictionary = dict(zip(values,keys))
    c = ''
    if choice.lower() == "word":
        for i in str:
            d = dictionary.get(i)
            c += d
        print(c)
    elif choice.lower() == "sentence":
        for i in str.split():
            for j in i:
                d = dictionary.get(j)
                c += d
            c += ' '
        print(c)

choice =  input(" If you to cipher a word enter 'word' or if you want cipher a sentence Enter 'Sentence' \n ")
str = input(" Enter string\n")
cipher(str, choice)

