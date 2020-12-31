def Advance_palindrome(phrase):
    import string
    b = string.punctuation
    p1 = []
    p2 = []
    for i in phrase.lower():
        if i !=' ' and i not in b:
            p1.append(i)
    p1.reverse()
    for i in phrase.lower():
        if i !=' ' and i not in b:
            p2.append(i)
    if p1 == p2:
        print('The string is palindrome')

phrase = input("Enter the String\n")
Advance_palindrome(phrase)