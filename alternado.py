def alternade(list):
    n = 2
    for word in list:
        fw = ''
        sw = ''
        for letter in word:
            n +=1
            if n%2 == 0:
                fw += letter
            else:
                sw += letter
        print(word,": makes",sw,'and',fw)



x = int(input('enter the number of list you want \n'))
list = []

for i in range(x):
    u = input("enter word \n")
    list.append(u)
print('list of words ', list)

alternade(list)