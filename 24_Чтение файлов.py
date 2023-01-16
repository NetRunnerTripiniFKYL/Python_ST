#В Python есть несколько методов чтения файла

"""
read - считывает содержимое файла в строку
readline - считывает файл построчно
readlines - считывает строки файла и создает список из строк
"""

#Метод read - считывает весь файл в одну строку

print (" \n#1")
file = open(r"A:\Users\lakus\Documents\Python\ST\List.txt", "r", encoding="utf8")  #Просто поставьте r перед вашей обычной строкой. Он преобразует обычную строку в необработанную строку
print (file.read())

#Построчно файл можно считать с помощью метода readline

print (" \n#2")
file = open(r"A:\Users\lakus\Documents\Python\ST\List.txt", "r", encoding="utf8")
print (file.readline())

#Еще один полезный метод - readlines. Он считывает строки файла в список

print (" \n#3")
file = open(r"A:\Users\lakus\Documents\Python\ST\List.txt", "r", encoding="utf8")
print (file.readlines())

"""
До сих пор, файл каждый раз приходилось открывать заново, чтобы снова его считать. 
Так происходит из-за того, что после методов чтения, курсор находится в конце файла. И повторное чтение возвращает пустую строку.
Чтобы ещё раз считать информацию из файла, нужно воспользоваться методом seek, который перемещает курсор в необходимое положение.
"""

print (" \n#4")

print (file.read())
print (file.read())
file.seek(0)
print (file.read())