print("1: подсчет гласных. ")
# УСЛОВИЕ: Подсчет гласных букв в строке.
# Примечание: - для простоты на вход принимаем строку из букв латинского алфавита;
# - набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
# - программа должна быть нечувствительна к регистру.
# Пример: assert vowels("hApPyHalLOweEn!") == 5
str1 = 'sOmewhere i bElong'
count = 0
vowels = 'aeiuoAEIOU'
for letter in str1:
    if letter in vowels:
        count += 1
print("Гласных: ", count)

#print(sum(letter in vowels for letter in str1))

print("")
print("2:  уникальный набор.")
# УСЛОВИЕ: Реализовать код, который принимает список елементов и убирает из него все дубликаты
# (формирует список уникальных элементов). Сделать вариант с сохранением порядка следования элементов и вариант,
# в кот. сортировка элементов не принципиальна.
# Пример: а) assert unique_ordered(["a", 5, 2, 5, (1, "a"), "a"]) == ["a", 5, 2, (1, "a")] б)
# assert unique_disordered(["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]

tup1 = (["a", 5, 2, 5, (1, "a"), "a"])
unique_ordered = []
for i in tup1:
    if i not in unique_ordered:
        unique_ordered.append(i)
print(unique_ordered)

unique_disordered = []

print("")
print("3: каждый третий: ")
# УСЛОВИЕ: Реализовать код который принимает кортеж и возвращает прореженный кортеж,
# оставляя только каждый третий элемент. Реализовать задачу двумя разными вариантами.
# Пример: assert thirds((1,2,3,4,5,6,7,8,9,0,'a','b','c')) == (3,6,9,'b')
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
print(tup[2:13:3])
# i = 0
# while i <= len(tup):
#     print(i[::2]) # каждый 3й эл-т

print("")
print("use Try- except: ")
# программа, зпрашивающая ввод 2х значений. Если хотя бы одно не является числом,
# то должна выполнятся конкатенация(соединене строк). В остальных случаях введенные числа суммируются.

first = input("Введите число или строку: ")
second = input("Введите еще строку или число: ")
try:
    res = int(first) + int(second)
except ValueError:
    res = first + second
print(res)

print("Задание 1: подсчет вхождений подстроки.  ")
# УСЛОВИЕ: Реализовать код, который будет подсчитывать "
#"количество вхождений подстроки "wow" в строке.  ВХОД: строка ВЫХОД: число вхождений подстроки "wow"  "
#     "Пример: assert wower("wowhatamanwowowpalehche") == 3  "

input_str = 'wowhatamanwowowpalehche'
res1 = input_str.count("wow")
print(res1)

# костыль
# res = 0
# for i in range(0, len(input_str) - 3):
#     if input_str[i : i + 3] == "wow":
#         res += 1
# print(res)


print("Задание 2: упорядоченная подстрока.")
# УСЛОВИЕ: Построить код, который будет находить в строке "
# "подстроку максимальной длины, в которой буквы упорядочены в алфавитном порядке.  "
# "ВХОД: строка ВЫХОД: подстрока  Пример: assert alphabetical("sabrrtuwacaddabra") == "abrrtuw"
abc = "sabrrtuwacaddabra"
final_out = ""
output = ""
prev = ""
for cur in abc:
    if cur >= prev:
        output += cur
        if len(final_out) < len(output):
            final_out = output
    else:
        output = cur
    prev = cur
print(final_out)



print()
print("чет-нечет")
# УСЛОВИЕ: Фрагмент кода, который принимает список любых чисел и фильтрует его по четным
# (удаляет нечетные), если количество элементов в списке является четным и наоборот (удаляет четные, если элементов изначально нечетное количество).
# assert evenodd_1([3, 7, 12]) == [3,7] assert evenodd_1([3, 7, 12, 7]) == [12]
# Решить задачу с помошью list comprehension.

list1_1 = [2, 7, 15, 22, 54, 99, 101]
list_out = [i for i in list1_1 if i % 2 == len(list1_1) % 2]
print(list_out)

print()
print("Триделение")
# СЛОВИЕ: Фрагмент кода, который принимает список любых чисел и возвращает словарь вида: {число: boolean},
# где: boolean - True или False в зависимости делится ли число на 3 без остатка.
# assert triples_1([3, 7, 12]) == {3: True, 12: True, 7: False} assert triples_1([9, 1, 2, 5, 9, 33]) == {1: False, 2: False, 5: False, 9: True, 33: True}
# Решить задачу двумя способами - с помощю dict. comprehension и без.

l_3 = range(7, 15)
l_out = {x: x % 3 == 0 for x in l_3}
print(l_out)