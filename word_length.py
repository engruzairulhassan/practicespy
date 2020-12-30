def word_length(list):
    b = []
    for i in list:
        count = 0
        for j in i:
            count += 1
        b.append(count)

    return b
list = []
y = int(input("Enter the length of list you want to add\n"))
for i in range(y):
    num = input("Enter the word\n")
    list.append(num)

print(word_length(list))