from functools import reduce


def check(a,b):
    u = a
    k = b
    if b > a:
        a = b
    return a


def max_in_list(list):
    k = reduce(check, list)
    print('Max in a list is  =',k)


x = int(input('Enter the number of list you want \n'))
list = []
for i in range(x):
    u = int(input("enter number \n"))
    list.append(u)
print('list of numbers ', list)
max_in_list(list)

