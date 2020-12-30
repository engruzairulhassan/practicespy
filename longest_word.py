def largest_word(list):
    b = []
    for i in list:
        count = 0
        for j in i:
            count += 1
        b.append(count)
    j = 0
    for m in b:
        for n in b:
            if n > m:
                j = n
    c = b.index(j)

    return c
list = []
y = int(input("Enter the length of list you want to add\n"))
for i in range(y):
    num = input("Enter the word\n")
    list.append(num)

print("The largest word is ",list[largest_word(list)])