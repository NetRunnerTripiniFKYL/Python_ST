list1 = [10, 10, 30, 40, 50, 50, 70, 80, 90, 90, 10]
set1 = set(list1) #С помощью множества можно легко убрать повторяющиеся элементы
print (f"#1 \nВывод: {set1} \n")

set1.add(100) #Метод add() добавляет элемент во множество
print (f"#2 \nВывод: {set1} \n")

set1.discard(99) #Метод discard() позволяет удалять элементы, не выдавая ошибку, если элемента в множестве нет
print (f"#3 \nВывод: {set1} \n")
set1.discard(100) 
print (f"#4 \nВывод: {set1} \n")

set1.clear() #Метод clear() очищает множество
print (f"#5 \nВывод: {set1} \n")

set2 = {10, 20, 30, 100}
set3 = {40, 50, 60, 100}

a = set2.union(set3) #Объединение множеств можно получить с помощью метода union() 
print (f"#6 \nВывод: {a} \n")
b = set2 | set3 #или оператора |
print (f"#7 \nВывод: {b} \n")

c = set2.intersection(set3) #Пересечение множеств можно получить с помощью метода intersection() 
print (f"#8 \nВывод: {c} \n")
b = set2 & set3 #или оператора &
print (f"#9 \nВывод: {b} \n")

#--------------------------------------------------------------------------------------------------------------------------------------------------

set4 = {} #Нельзя создать пустое множество с помощью литерала (так как в таком случае это будет не множество, а словарь)
print(f"#10 \nВывод: {type(set4)} \n")

set4 = set() #Но пустое множество можно создать таким образом
print (f"#11 \nВывод: {type(set4)} \n")

text1 = "Hi Hello hi hello H 10,20,30,100-200"
d = set(text1) #Множество из строки
print (f"#12 \nВывод: {d} \n")