"""
4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
           'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
           'nine': 'девять', 'ten': 'десять'}

my_f = open('4.txt', encoding='utf-8')
content = my_f.readlines()
my_f.close()
print(content)

my_newfile = open('new4.txt', 'w', encoding='utf-8')
for el in content:
    my_newfile.write(my_dict[el[:el.find(' ')].lower()] + el[el.find(' '):])
my_newfile.close()