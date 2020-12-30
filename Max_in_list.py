def max_in_list(list):
    b = 0
    for i in list:
        for j in list:
            if j > i:
                b = j
    print('Max in list is', b)

list = []
y = int(input("Enter the length of list you want to add\n"))
for i in range(y):
    num = int(input("Enter the word\n"))
    list.append(num)
max_in_list(list)
