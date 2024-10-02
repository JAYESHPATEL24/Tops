with open("C:\\Users\\jayes\\Documents\\Tops\\Tops\\Python\\Class Work\\12.02-10-2024(Wendsday)\\Good.txt","w+") as file:
    file.write("Hello Beautiful World!!!!!!")
    print(file.tell())
    file.seek(0)
    print(file.readline())
    