# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_f = open('2.txt', encoding='utf-8')
content = my_f.readlines()
my_f.close()
print(content)
print(f'Количество строк = {len(content)}')
for el in content:
    if el == '\n' or el == '':
        print(f'Количество слов в {content.index(el) + 1} '
              f'строке = {0}')
    else:
        print(f'Количество слов в {content.index(el) + 1} '
              f'строке = {el.count(" ") + 1}')
