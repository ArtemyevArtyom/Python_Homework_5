# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    line = input(" Введите данные латиницей: ")
    if line == '':
        exit()
    else:
        new_line = line + '\n'
        my_list.append(new_line)
    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)
