text1 = "Hi, my name {0}".format("Trip", "2342342") #Пример использования метода format
print (f"#1 \nВывод: {text1} \n")

text2 = "---{0}---" #Значения, которые подставляются в фигурные скобки, могут быть разного типа. Например, это может быть строка, число или список или даже словарь
print ("#2 \nВывод: " + text2.format([10, 20, 30, 40, 50]) + "\n")
print ("#3 \nВывод: " + text2.format(500_000) + "\n")
print ("#4 \nВывод: " + text2.format({"name" : "Trip", "sex" : True}) + "\n")

list1 = [10, 20, 30] #Можно вывести данные столбцами одинаковой ширины по 15 символов с выравниванием по правой стороне
a = list1[0]
b = list1[1]
c = list1[2]
print ("#5 \nВывод: " + "{2:>5} {0:>5} {1:>5}".format(a, b, c) + "\n")

ip_sample = """
IP address :
{0}
"""
ip1 = "345.624.534.5"
ip2 = "423.234.456.7"
ip3 = "234.456.234.2"
ip4 = "745.523.235.8"
print ("#6 \nВывод: " + ip_sample.format(ip1) + "\n") #Шаблон для вывода может быть и многострочным

text3 = "Pay me {:.3f}" #Например, можно указать, сколько цифр после запятой выводить
print ("#7 \nВывод: " + text3.format(500_000 / 25) + "\n")

print ("#8 \nВывод: " + "{0:b} {1:b} {2:b}".format(10, 20, 30) + "\n") #С помощью форматирования строк можно конвертировать числа в двоичный формат

text4 = "---{ip}---   ---{mask}---" #В фигурных скобках можно указывать имена. Это позволяет передавать аргументы в любом порядке, а также делает шаблон более понятным
print ("#9 \nВывод: " + text4.format(ip = ip1, mask = 50) + "\n") 

ip_template = """
IP address
{0} {1} {2} {3}
{0:>15} {1:>15} {2:>15} {3:>15}
{0:>25} {1:>25} {2:>25} {3:>25}
"""
print ("#10 \nВывод: " + ip_template.format(ip1, ip2, ip3, ip4) + "\n")