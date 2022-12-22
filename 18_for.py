"""
Очень часто одно и то же действие надо выполнить для набора однотипных данных. 
Например, преобразовать все строки в списке в верхний регистр. Для выполнения таких действий в Python используется цикл for.
Цикл for перебирает по одному элементы указанной последовательности и выполняет действия, которые указаны в блоке for, для каждого элемента.

Примеры последовательностей элементов, по которым может проходиться цикл for:

строка
список
словарь
Функция range
любой Итерируемый объект 
"""

#Пример преобразования строк в списке в верхний регистр:

print (" \n#1")

list = ["kerb", "trip", "don"]
upper_list = []

for word in list:
    upper_list.append(word.upper())

print (upper_list)

#При работе со строками, цикл for перебирает символы строки, например:

print (" \n#2")

text = "Trip"

for letter in text:
    print (letter)

#Иногда в цикле необходимо использовать последовательность чисел. В этом случае, лучше всего использовать функцию Функция range

#Пример цикла for с функцией range():

print (" \n#3")

for a in range(101): 
    print (f"Loading {a}%") #Обратите внимание что требуется f

#В этом цикле используется range(101). Функция range генерирует числа в диапазоне от нуля до указанного числа (в данном примере - до 101), не включая его.

#В этом примере цикл проходит по списку VLANов, поэтому переменную можно назвать vlan:

print (" \n#4")

vlans = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for vlan in vlans:
    print (f"vlan{vlan}")
    print (f"name_of_vlan{vlan}\n")

#Когда цикл идет по словарю, то фактически он проходится по ключам:

print (" \n#5")

owners_NR = {
    "Trip": {
        "location": "Russia",
        "sex": "Men",
        "model_pc/laptop": "Laptop",
        "ip": "130.255.034.13"
    },
    "Kerb": {
        "location": "Russia",
        "sex": "Men",
        "model_pc/laptop": "Laptop",
        "ip": "130.255.06642"
    },
    "Don": {
        "location": "Kazakstan",
        "sex": "Men",
        "model_pc/laptop": "PC",
        "ip": "160.255.023.101"
    }
}

for keys in owners_NR:
    print (keys)

#Если необходимо выводить пары ключ-значение в цикле, можно делать так:

print (" \n#6")

for key in owners_NR:
    print (key + "=>", owners_NR[key])

#---------------------------------------------------------------------------------------

#Циклы for можно вкладывать друг в друга

print (" \n#7")

commands = ["switchport mode access" , "spanning-tree portfas" , "spanning-tree bpduguard enable"]
fast_int = ["0|1" , "1|2" , "2|3"]

for intf in fast_int:
    print('interface FastEthernet {}'.format(intf))
    for command in commands:
        print(' {}'.format(command))

#Рассмотрим пример совмещения for и if

print (" \n#8")

access_template = ['switchport mode access',
'switchport access vlan',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

access = {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

#Комментарии к коду:

"""
В первом цикле for перебираются ключи и значения во вложенном словаре access
Текущий ключ, на данный момент цикла, хранится в переменной intf
Текущее значение, на данный момент цикла, хранится в переменной vlan
Выводится строка interface FastEthernet с добавлением к ней номера интерфейса
Во втором цикле for перебираются команды из списка access_template
Так как к команде switchport access vlan надо добавить номер VLAN:
внутри второго цикла for проверяются команды
если команда заканчивается на access vlan
выводится команда, и к ней добавляется номер VLAN
во всех остальных случаях просто выводится команда
"""