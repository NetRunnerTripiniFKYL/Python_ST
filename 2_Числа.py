a = 5 #int (целые числа)
b = 10
c = 20 
d = 3.33333 #float (числа с плавающей точкой)
f = "100"
k = 77 + 77j #complex (комплексные числа)

print (a * c) #Умножаем 

print (a ** 2) #Возводим в степень 

print (c % d) #Остаток от деления 

round_ex = round(d) #Округляем функция round
print (round_ex)

print (a >= d) #Сравниваем (выводит булиевые значения)

f = int(f) #Функция int() позволяет выполнять конвертацию в тип int
print (f)

d = int(d) #Конвертация в int типа float
print (d)

v = bin(a) #Функция bin позволяет получить двоичное представление числа (обратите внимание, что результат - строка)
print (v)

h = hex(b) #Функция hex() позволяет получить шестнадцатеричное значение
print (h)

print (k * 2)