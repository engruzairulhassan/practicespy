def is_member(x,n):
    for i in x:
        if n == i:
            global b
            print(n, b)
            break
    else:
        print('not a member')

selection = int(input("Enter a string or list of number\nFor String Enter 1 and for list Enter 2\n"))
if selection == 1:
    x = input("Enter the string\n")
    n = input("Enter the which you want to check\n")
    b = " The letter is the member of the string"
    is_member(x, n)
elif selection == 2:
    x = []
    y = int(input("Enter the length of list you want to add\n"))
    for i in range(y):
        num = input("Enter the number\n")
        x.append(num)
    n = input("Enter the which you want to check\n")
    b = " The number is member of the list"
    is_member(x, n)
else:
    print('invalid Selection')


