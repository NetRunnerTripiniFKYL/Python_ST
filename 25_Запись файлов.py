"""
При записи, очень важно определиться с режимом открытия файла, чтобы случайно его не удалить:

w - открыть файл для записи. Если файл существует, то его содержимое удаляется
a - открыть файл для дополнения записи. Данные добавляются в конец файла

При этом оба режима создают файл, если он не существует.

Для записи в файл используются такие методы:

write - записать в файл одну строку
writelines - позволяет передавать в качестве аргумента список строк
"""
#Метод write ожидает строку, для записи

file = open(r"A:\Users\lakus\Documents\Python\ST\List2.txt", "r+", encoding="utf8")
file.write("juice")
file.close()

#Метод writelines ожидает список строк, как аргумент

new_list = ["bobs", "\nfish"]

file = open(r"A:\Users\lakus\Documents\Python\ST\List2.txt", "r+", encoding="utf8")
file.writelines(new_list)
file.close()
