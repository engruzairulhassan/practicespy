def Transform(list):
    T_list = []
    for i in list:
        length = len(i)
        T = ''
        x = ''
        b = ["o", "s", "x", "z"]
        for j in i:
            if length == 1:
                if j == "y":
                    T += 'ies'
                elif j in b or (x == "c" and j == "h") or (x == "s" and j == "h"):
                    T += j
                    T += 'es'
                else:
                    T += j
                    T += 's'
            else:
                T += j
                x = j
            length -= 1
        T_list.append(T)
    print('list of transformed word',T_list)
x = int(input('This code is to find the third person Transform of verb \nEnter the number of list you want \n'))
list = []
for i in range(x):
    u = input("enter word \n")
    list.append(u)
print('list of word ', list)
Transform(list)



