pers1 = {"Name" : "Trip", "Ip" : "123.543.466.5", "Sex" : "Man", "Town" : "Novosib"} #Словари - это изменяемый упорядоченный тип данных

pers1 = {
"Name" : "Trip", 
"Ip" : "123.543.466.5", 
"Sex" : "Man", 
"Town" : "Novosib"} #Можно записывать и так

print (pers1["Ip"]) #Для того, чтобы получить значение из словаря, надо обратиться по ключу, таким же образом, как это было в списках, только вместо номера будет использоваться ключ
print (pers1["Town"])

pers1["Port"] = "8080" #Аналогичным образом можно добавить новую пару ключ-значение
print (pers1)

print (sorted(pers1)) #Функция sorted сортирует ключи словаря по возрастанию и возвращает новый список с отсортированными ключами

pers1.clear() #Метод clear позволяет очистить словарь
print (pers1)

pers2 = {"Name" : "Kerb", "Ip" : "345.867.345.5", "Sex" : "Man", "Town" : "Moscow"}

pers2v2 = pers2.copy() #Метод copy позволяет создать полную копию словаря
print (pers2v2)

pers2v2["Port"] = "8080" #Если мы добавим в новый словарь ключ + значение то на первый словарь это не повлияет
print (pers2, pers2v2)

print (pers2.get("Name")) #Метод get запрашивает ключ, и если его нет, вместо ошибки возвращает None

print (pers2.get("Port", "Ключ не найден\nДобавить? [y/n]"))

pers2v2.setdefault("Has_child") #Метод setdefault ищет ключ, и если его нет, вместо ошибки создает ключ со значением
print (pers2v2)

print (pers2v2.keys()) #Методы keys, values, items
print (pers2v2.values())
print (pers2v2.items()) #Все три метода возвращают специальные объекты view, которые отображают ключи, значения и пары ключ-значение словаря соответственно

del pers2["Town"] #del Удалить ключ и значение
print (pers2)

pers1.update(pers2) #Метод update позволяет добавлять в словарь содержимое другого словаря
print (pers1)

pers1.update(pers2v2) #Аналогичным образом можно обновить значения
print (pers1)