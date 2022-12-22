#В циклах for и while опционально может использоваться блок else
"""
В цикле for:

блок else выполняется в том случае, если цикл завершил итерацию списка
но else не выполняется, если в цикле был выполнен break
"""
#for/else -------------------------------------------------------------------------

#Пример цикла for с else (блок else выполняется после завершения цикла for):

print (" \n#1")

for num in range(5):
     print(num)
else:
     print("Числа закончились")

#Пример цикла for с else и break в цикле (из-за break блок else не выполняется):

print (" \n#2")

for num in range(5):
    if num == 3:
        break
    else:
        print(num)
else:
    print("Числа закончились")

#Пример цикла for с else и continue в цикле (continue не влияет на блок else):

print (" \n#3")

for num in range(5):
    if num == 3:
         continue
    else:
         print(num)
else:
    print("Числа закончились")

#while/else -------------------------------------------------------------------------

"""
В цикле while:

блок else выполняется в том случае, если условие в while ложно
else не выполняется, если в цикле был выполнен break
"""
#Пример цикла while с else (блок else выполняется после завершения цикла while):

print (" \n#4")

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Конец")

#Пример цикла while с else и break в цикле (из-за break блок else не выполняется):

print (" \n#5")

i = 0

while i < 5:
    if i == 3:
        break
    else:
        print(i)
        i += 1
else:
     print("Конец")

