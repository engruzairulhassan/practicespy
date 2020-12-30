def Generate_n_chars(Int, Chr):
    for i in range(Int):
        print(Chr, end="")
Int = int(input("Enter the integer\n"))
Chr = input("Enter the character\n")
Generate_n_chars(Int, Chr)