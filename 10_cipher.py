import random # импортируем модуль для генерации случайных чисел
#flag = True
stone_key = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # список возможных чисел
stone_pass = [] # Список пароль заполняется в ходе программы
key_ = random.choice(stone_key)  #  выбор случайного числа из списка stone_key
for i in range(1, key_): # проходим все значения исключая ноль до key_(наше случайное число)
    #if flag == False: # выход из основного цикла
        #break
    for j in range(2, key_): # проходим все значения исключая 0 и 1 до key_(наше случайное число)
        if [j, i] in stone_pass: # проверяем содержит ли наш список такую пару?
            #flag = False # для выхода из основного цикла
            continue #  выход из подцикла
        else: # Если пара уникальная продолжаем
            if key_ % sum([i, j]) == 0 and i != j: # Проверяем остаток от деления нашего числа на сумму пары и чтоб числа были не одинаковые
                stone_pass.append([i, j]) # если без остатка то вносим пару в список
print('Число ключ:', key_) # выводим какой ключ у нас выпал рандомно
print("Пароль: ", end='')
#print("Пароль", *stone_pass) # пытался вывести список без скобок но подсписки все равно со скобками
for i in stone_pass: #Вывод пароля в строчку без запятых
    for j in i:
        print(j, end='')

        #### ###### ########

        # Ниже попытки вывести список единой строкой без [] , ''
#print(''.join([''.join(i) for i in stone_pass[i]]))
#print('\n'.join([', '.join(i) for i in x]))
#list = [1, 2]
#print(map(str, list)
# pokemon_list = [1, 2]
# print(''.join(str(pokemon_list)))
#numbers1 = [[1,5], [2], [3]]
# result = map(lambda x: str(x[0]), numbers1)
# print(''.join(result))
