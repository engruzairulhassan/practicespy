def checker(string):
    string1 = ""
    count = 0
    j = " "
    for i in string:
        if j == " " and i == " ":
            if count == 0:
                count -= 1
            pass
        elif count == 0 or j == '.':
            i = i.upper()
            string1 += i
        elif i == ".":
            string1 += i
            string1 += " "
        else:
            string1 += i
        j = i
        count += 1
    print(string1)
string = input("Enter the string you want to correct")
checker(string)