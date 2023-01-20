#Иногда нужно работать одновременно с двумя файлами. Например, надо записать некоторые строки из одного файла, в другой

#В таком случае, в блоке with можно открывать два файла таким образом

with open(r"A:\Users\lakus\Documents\Python\ST\r1.txt", "r") as a, open(r"A:\Users\lakus\Documents\Python\ST\List.txt", "w") as b:
    for line in a:
        if line.startswith("service"): #Тут мы записали в другой файл только первые 4 строки, так как указали что переписывать только если строка начинается с service
            b.write(line)

