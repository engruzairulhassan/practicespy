def make_ing_form(list):
    T_list = []
    for i in list:
        length = len(i)
        cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vow = ['a', 'e', 'i', 'o', 'u']
        T = ''
        x = ''
        b = ["o", "s", "x", "z"]
        for j in i.lower():
            if length == 3:
                y = j
            if length == 1:
                if j == "e":
                    T += 'ing'
                elif x == "i" and j == "e":
                    T += "y"
                    T += 'ing'
                elif y in cons and x in vow and j in cons:
                    T += j
                    T += j
                    T += 'ing'
                else:
                    T += j
                    T += 'ing'
            else:
                T += j
                x = j
            length -= 1
        T_list.append(T)
    print('list of present participle form',T_list)
x = int(input('This code is to give the present participle form of verb \nEnter the number of list you want \n'))
list = []
for i in range(x):
    u = input("enter word \n")
    list.append(u)
print('list of word ', list)
make_ing_form(list)



