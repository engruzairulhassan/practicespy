def max(list):
    for i in list:
        pass

x = int(input('enter the number of list you want \n'))
list = []
for i in range(x):
    u = int(input("enter number \n"))
    list.append(u)
print('list of numbers ', list)
max(list)