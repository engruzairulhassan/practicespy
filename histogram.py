def histogram(list):
    for i in list:
        for a in range(i):
            print('x', end="")
        print('\n')
x = int(input('enter the number of list you want \n'))
list = []
for i in range(x):
    u = int(input("enter number \n"))
    list.append(u)
print('list of numbers ', list)
histogram(list)