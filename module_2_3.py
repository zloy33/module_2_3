my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # список
x = 0 # обращение к индексу из списка
while x < len(my_list): # условие прекращения цикла
    if my_list[x] >= 0:
        if my_list[x] != 0:
            print(my_list[x])
        x = x + 1 # изменение значения переменной( индекса из списка)
        continue
    else:
        break
    # для понятия как работает обращение к индексу
# x = 0
# print(my_list[x])
# x = x + 1
# print(my_list[x])
# x = x + 1
# print(my_list[x])
# x = x + 1
# print(my_list[x])