def sort(c):
    l = len(c)
    for i in range(l):
        min = i
        for j in range(i, l):
            a = c[j]
            b = c[min]
            if a < b:
                min = j
        c[min], c[i] = c[i], c[min]
    return c



def search(b, a):
    low = b[0]
    l = len(b)
    l = l - 1
    hig = b[l]
    if low == a:
        global i
        i = b.index(a)
        return True
    elif hig == a:
        i = b.index(a)
        return True
    elif a >= low and a <= hig:
        avg1 = (low+hig)/2
        avg = int(avg1)
        while avg != a:
            if a > avg:
                low = avg
            else:
                hig = avg
            avg = int((low + hig) / 2)
        if avg == a:
            i = b.index(a)
            return True
    else:
        return False



x = int(input('enter the number of list you want \n'))
list = []
for i in range(x):
    u = int(input("enter number \n"))
    list.append(u)
print('list of numbers ', list)
b = sort(list)
print('Sorted list ', b)
a = int(input('enter the number you want to search \n'))
i = -1
if search(b,a):
    print('number found at index no ', i)
else:
    print('number not found')