#Конструкция if/elif/else позволяет делать ответвления в ходе программы. Программа уходит в ветку при выполнении определенного условия.
#В этой конструкции только if является обязательным, elif и else опциональны:

#Проверка if всегда идет первой.
#После оператора if должно быть какое-то условие: если это условие выполняется (возвращает True), то действия в блоке if выполняются.
#С помощью elif можно сделать несколько разветвлений, то есть, проверять входящие данные на разные условия.
#Блок elif это тот же if, но только следующая проверка. Грубо говоря, это «а если …»
#Блоков elif может быть много.
#Блок else выполняется в том случае, если ни одно из условий if или elif не было истинным.

#Пример конструкции:

print (" \n#1")

sum = 51
comparison = 60

if sum == comparison:
    print ("Сумма равна {0}".format(comparison))
elif sum > comparison:
    print ("Сумма больше {0}".format(comparison))
elif sum < comparison:
    print ("Сумма меньше {0}".format(comparison))

"""
В Python, кроме очевидных значений True и False, всем остальным объектам также соответствует ложное или истинное значение: 

#истинное значение:

#любое ненулевое число
#любая непустая строка
#любой непустой объект

#ложное значение:

#0
#None
#пустая строка
#пустой объект
"""
#Например, так как пустой список это ложное значение, проверить, пустой ли список, можно таким образом:

print (" \n#2")

list = [100, 500]

if list:
    print ("Это не пустой список")
else:
    print ("Это пустой список")