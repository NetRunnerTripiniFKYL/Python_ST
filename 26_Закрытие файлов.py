"""
После завершения работы с файлом, его нужно закрыть. В некоторых случаях Python может самостоятельно закрыть файл.
Но лучше на это не рассчитывать и закрывать файл явно.
"""

#У объекта file есть специальный атрибут closed, который позволяет проверить, закрыт файл или нет. Если файл открыт, он возвращает False

file = open(r"A:\Users\lakus\Documents\Python\ST\List2.txt", "r+", encoding="utf8")
print (file.closed)
file.close()
print (file.closed)