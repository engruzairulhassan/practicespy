def translator(string):
    dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    c = ''
    for i in string.split():
        d = dictionary.get(i)
        c += d + ' '
    print(c)
string = input(" Enter 'merry christmas and happy new year' to its swedish translation\n")
translator(string)