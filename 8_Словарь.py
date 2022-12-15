pers1 = {"Name" : "Trip", "Ip" : "123.543.466.5", "Sex" : "Man", "Town" : "Novosib"} #Словари - это изменяемый упорядоченный тип данных

pers1 = {
"Name" : "Trip", 
"Ip" : "123.543.466.5", 
"Sex" : "Man", 
"Town" : "Novosib"} #Можно записывать и так

print (f"#1 \nВывод: " + pers1["Ip"] + "\n") #Для того, чтобы получить значение из словаря, надо обратиться по ключу, таким же образом, как это было в списках, только вместо номера будет использоваться ключ
print (f"#2 \nВывод: " + pers1["Town"] + "\n")

pers1["Port"] = "8080" #Аналогичным образом можно добавить новую пару ключ-значение
print (f"#3 \nВывод: {pers1} \n")

print (f"#4 \nВывод: {sorted(pers1)} \n") #Функция sorted сортирует ключи словаря по возрастанию и возвращает новый список с отсортированными ключами

pers1.clear() #Метод clear позволяет очистить словарь
print (f"#5 \nВывод: {pers1} \n")

pers2 = {"Name" : "Kerb", "Ip" : "345.867.345.5", "Sex" : "Man", "Town" : "Moscow"}

pers2v2 = pers2.copy() #Метод copy позволяет создать полную копию словаря
print (f"#6 \nВывод: {pers2v2} \n")

pers2v2["Port"] = "8080" #Если мы добавим в новый словарь ключ + значение то на первый словарь это не повлияет
print (f"#7 \nВывод: {pers2, pers2v2} \n")

print (f"#8 \nВывод: " + pers2.get("Name") + "\n") #Метод get запрашивает ключ, и если его нет, вместо ошибки возвращает None

print (f"#9 \nВывод: " + pers2.get("Port", "Ключ не найден\nДобавить? [y/n]") + "\n")

pers2v2.setdefault("Has_child") #Метод setdefault ищет ключ, и если его нет, вместо ошибки создает ключ со значением
print (f"#10 \nВывод: {pers2v2} \n")

print (f"#11 \nВывод: {pers2v2.keys()} \n") #Методы keys, values, items
print (f"#12 \nВывод: {pers2v2.values()} \n")
print (f"#13 \nВывод: {pers2v2.items()} \n") #Все три метода возвращают специальные объекты view, которые отображают ключи, значения и пары ключ-значение словаря соответственно

del pers2["Town"] #del Удалить ключ и значение
print (f"#14 \nВывод: {pers2} \n")

pers1.update(pers2) #Метод update позволяет добавлять в словарь содержимое другого словаря
print (f"#15 \nВывод: {pers1} \n")

pers1.update(pers2v2) #Аналогичным образом можно обновить значения
print (f"#16 \nВывод: {pers1} \n")