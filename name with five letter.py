x = int(input('enter the no, of list of string you want to add\n'))
b = []
for i in range(x):
    u = input("enter the name \n")
    b.append(u)
print(b)
c = 0

def count(b):
    for i in b:
        p = 0
        for m in i:
            p += 1
            if p == 5:
                global c
                c += 1
count(b)
print('there are ', c, 'words with five or more letters in this list ')
