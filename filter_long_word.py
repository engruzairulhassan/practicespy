def largest_word(list,n):

    for i in list:
        p = 0
        for m in i:
            p += 1
            if p == n:
                global b
                global c
                b.append(i)
                c += 1
    return c, b
c  = 0
b = []
list = []
y = int(input("Enter the length of list you want to add\n"))
for i in range(y):
    num = input("Enter the word\n")
    list.append(num)
n = int(input("Enter the no to which you want to check\n"))
largest_word(list,n)
print('there are ', c, 'words with five or more letters in this list ',b)