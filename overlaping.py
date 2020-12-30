def overlaping(list1,list2):
    for i in list1:
        for b in list2:
            if b == i:
                return True
                break
    return False

list1 = []
x = int(input("Enter the length of list1 you want to add\n"))
for i in range(x):
    num = input("Enter the number of list 1\n")
    list1.append(num)
list2 = []
y = int(input("Enter the length of list2 you want to add\n"))
for i in range(y):
    num = input("Enter the number of list 2\n")
    list2.append(num)

b = overlaping(list1,list2)
print('The condition overlapping is ', b)