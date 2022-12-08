print ("a".isdigit()) #Чтобы проверить, состоит ли строка из одних цифр, можно использовать метод isdigit
print ("a10".isdigit())
print ("10".isdigit())

print ("a".isalpha()) #Метод isalpha позволяет проверить, состоит ли строка из одних букв
print ("a100".isalpha())
print ("a100".isalpha())

print ("a".isalnum()) #Метод isalnum позволяет проверить, состоит ли строка из букв или цифр
print ("a10".isalnum())

print (type("string")) #Иногда, в зависимости от результата, библиотека или функция может выводить разные типы объектов. В этом может помочь функция type
print (type("string") == str) 

print (type((1,2,3))) #Аналогично с кортежем (и другими типами данных)
print (type((1,2,3)) == tuple)
print (type((1,2,3)) == list)