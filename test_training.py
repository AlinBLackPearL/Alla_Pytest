from random import random
# str1 = [elem for elem in 'ecnalubma']
# for item in range(len(str1)):
#     print(str1[-(item+1)])

# str2 = [elem for elem in 'ecnalubma']
# str2.reverse()
# print(str2)
print("1 - Реверс строки. input: 'ecnalubma'; output: 'ambulance''")

str3 = [elem for elem in 'ecnalubma']
str4 = str3[::-1]
str4_str = ""
for i in str4:
    str4_str += str(i) + " "
str4_str = str4_str[:-1]
print(str4_str)

# or
str3 = [elem for elem in 'ecnalubma']
str4 = str3[::-1]
str4 = ''.join(map(str, str4))
print(str4)
print()

print("2 - Реверс строки 2. input: 'one two three four'; output: 'four three two one'")
str5 = ['one', 'two', 'three', 'four']
str5_1 = str5[::-1]
print(str5_1)
print()

print("3 - сумма 3х зн случ, числа")
num = random() * 900 + 100
num = int(num)
print("random digit:", num)
first = num // 100
second = (num // 10) % 10
third = num % 10
print("summ of random digits:", (first + second + third))

print()
print("4 - в сгенерированном списке подсчитать чет и нечет")
chet = 0
nechet = 0
for i in range(7, 20):
    if int(i) % 2 == 0:
        chet += 1
    else:
        nechet += 1
print("Чётных чисел:", chet, "Не чётных чисел: ", nechet)

print()
print("5 - Заменить отрицательные числа в списке на -1, положительные - на число 1, ноль оставить без изменений.")
list1 = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
list2 = []
for i in list1:
    if i < 0:
        list2.append(-1)
    elif i > 0:
        list2.append(1)
    else:
        list2.append(0)

print("Заданный список", list1)
print("Измененный список", list2)


print()
print("Home work - Sets & Dicts")
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
    print(x)
#print(thisdict)

print()
print("Добавление эл-ов в Словарь")
dict1 = {0: 10, 1: 20}
dict1[2]