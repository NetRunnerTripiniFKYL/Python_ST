#Для работы с исключениями используется конструкция try/except:

print (" \n#1")

try:
     2/0
except ZeroDivisionError:
    print("You can't divide by zero")

"""
Конструкция try работает таким образом:

сначала выполняются выражения, которые записаны в блоке try
если при выполнения блока try не возникло никаких исключений, блок except пропускается, и выполняется дальнейший код
если во время выполнения блока try в каком-то месте возникло исключение, оставшаяся часть блока try пропускается
если в блоке except указано исключение, которое возникло, выполняется код в блоке except
если исключение, которое возникло, не указано в блоке except, выполнение программы прерывается и выдается ошибка
"""

#Обратите внимание, что строка Cool! в блоке try не выводится:

print (" \n#2")

try:
    print("Let's divide some numbers")
    2/0 #Попробуй поменять 0 на что то другое и поймешь
    print('Cool!')
except ZeroDivisionError:
    print("You can't divide by zero")

#Если нет необходимости выводить различные сообщения на ошибки ValueError и ZeroDivisionError, можно сделать так

print (" \n#3")

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")

#В конструкции try/except есть опциональный блок else. Он выполняется в том случае, если не было исключения.

#Например, если необходимо выполнять в дальнейшем какие-то операции с данными, которые ввел пользователь, можно записать их в блоке else

print (" \n#4")

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)

#Блок finally. Он выполняется всегда, независимо от того, было ли исключение или нет.

#Сюда ставятся действия, которые надо выполнить в любом случае. Например, это может быть закрытие файла.

print (" \n#5")

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Программа выполнена.")