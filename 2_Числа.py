a = 5 #int (целые числа)
b = 10
c = 20 
d = 3.33333 #float (числа с плавающей точкой)
f = "100"
k = 77 + 77j #complex (комплексные числа)

print (f"#1 \nВывод: {a * c} \n") #Умножаем 

print (f"#2 \nВывод: {a ** 2} \n") #Возводим в степень 

print (f"#3 \nВывод: {c % d} \n") #Остаток от деления 

round_ex = round(d) #Округляем функция round
print (f"#4 \nВывод: {round_ex} \n")

print (f"#5 \nВывод: {a >= d} \n") #Сравниваем (выводит булиевые значения)

f = int(f) #Функция int() позволяет выполнять конвертацию в тип int
print (f"#6 \nВывод: {f} \n")

d = int(d) #Конвертация в int типа float
print (f"#7 \nВывод: {d} \n")

v = bin(a) #Функция bin позволяет получить двоичное представление числа (обратите внимание, что результат - строка)
print (f"#8 \nВывод: {v} \n")

h = hex(b) #Функция hex() позволяет получить шестнадцатеричное значение
print (f"#9 \nВывод: {h} \n")

print (f"#10 \nВывод: {k * 2} \n")