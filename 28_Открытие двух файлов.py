#Иногда нужно работать одновременно с двумя файлами. Например, надо записать некоторые строки из одного файла, в другой

#В таком случае, в блоке with можно открывать два файла таким образом

with open(r"A:\Users\lakus\Documents\Python\ST\r1.txt", "r") as a, open(r"A:\Users\lakus\Documents\Python\ST\List.txt", "w") as b:
    for line in a:
        if line.startswith("service"):
            b.write(line)