def palindrome(word):
    check_word = ""
    length = len(word)
    b = [None]*length
    for letter in word:
        b[length-1] = letter
        length -=1
    for i in b:
        check_word += i
    if word == check_word:
        print('the word ', word, 'is a palindrome')
    else:
        print('the word is not a palindrome')
word = input('Enter the word \n')
palindrome(word)




