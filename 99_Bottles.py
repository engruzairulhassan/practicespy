def bottle_99(x):
    n = 99
    for i in range(n):
        print(n, 'bottles of beer on the wall,',n, 'bottles of beer. Take one down, pass it around,')
        n -= 1
x = input('Write "start" to see the lyrics\n')
if x.lower() == "start":
    bottle_99(x)
else:
    print("Entered wrong string")