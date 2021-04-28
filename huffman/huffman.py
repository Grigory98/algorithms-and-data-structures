input_list = input('Слово: ')
input_list = list(input_list)

inp_str = input_list
dictionary = {}
p = []
s = []
set1 = set(input_list)
c1 = list(set1)

end_str = ""
empt = ""

print("Выводим только уникальные значения списка: " + str(c1))
for key in set1:
    cnt = 0
    for num in input_list:
        if num == key:
            cnt += 1
    p.append(round(cnt / len(input_list), 5))
    s.append("")

code_dict = dict(zip(c1, s))
temp_dict = dict(zip(c1, p))

# Сортировка
list_slov = list(temp_dict.items())
list_slov.sort(key=lambda temp_dict: temp_dict[1], reverse=True)

for i in list_slov:
    dictionary.update({i[0]: i[1]})
print("Сортируем словарь: " + str(dictionary))

# 2 самых маленьких складываем, снова сортируем и т д
temp_dict = list(dictionary.items())
print("Преобразовываем словарь в список: " + str(temp_dict))
lenght = len(temp_dict)
print("Складываем два последних значения списка,сортируем по убыванию:")
for i in range(lenght):
    count = (len(temp_dict) - 1)
    a = temp_dict[count][0] + temp_dict[count - 1][0]  # 5 элемент массива плюс 4 элемент массива(буквы)
    print(code_dict)
    for key in code_dict:
        if temp_dict[count][0].find(key) != -1:
            code_dict[key] += '1'
        if temp_dict[count - 1][0].find(key) != -1:
            code_dict[key] += '0'

    b = temp_dict[count][1] + temp_dict[count - 1][1]  # 5 элемент массива плюс 4 элемент массива(значения)
    del temp_dict[count]
    del temp_dict[count - 1]
    temp_dict.append((a, b))
    temp_dict.sort(key=lambda temp_dict: temp_dict[1], reverse=True)
    if i == lenght - 2:
        break
#print(temp_dict)
#print(code_dict)

for i in inp_str:
    for j in code_dict:
        if j == i:
            end_str += code_dict[j]
print("Конечная строка: " + end_str)

# Декодирование
while end_str != "":
    for i in code_dict:
        index = end_str.find(code_dict[i])
        if index == 0:
            end_str = end_str[len(code_dict[i]):]
            empt += i
print("Декодированное сообщение: "+empt)
