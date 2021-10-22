print('1. Дано целое число (int). Определить сколько нулей в этом числе.')

1
variant

number = str(102304005)
find = "0"
result = number.count(find)
print(f"Number of 0: {result}")

2
variant

your_number = input("Enter your number with 0: ")
result = your_number.count("0")
print(f"Number of 0: {result}")

print(' Дано целое число (int). Определить сколько нулей в конце этого числа.')

1
variant

number = 28018102300000
numb_zero = 0
while number % 10 == 0:
    number //= 10
    numb_zero += 1
print(f"Number of 0: {numb_zero} ")

2
variant

number = input("Enter your number with 0: ")
result = len(number) - len(number.rstrip("0"))
print(f"Number of 0 in the end: {result} ")

print(
    '3. Дана строка в которой есть числа (разделяются пробелами).Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.Для данного примера ответ - 133. (используйте split и проверку isdigit)')

str_1 = "43 больше чем 34 но меньше чем 56"
res_numb = []
our_list = str_1.split()
for number in our_list:
    if number.isdigit():
        res_numb.append(int(number))
result = sum(res_numb)
print(result)

print(
    '4. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,которые точно находятся в этой строке. Причем l_limit левее чем r_limit.В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.my_str = "My long string", l_limit = "o",r_limit = "g" -> sub_str = "ng strin".')

my_str = "My long string"
l_limit = "o"
r_limit = "g"
for nol in my_str:
    if nol != l_limit:
        new_str = my_str[my_str.index(l_limit):]
result = new_str.rstrip(r_limit)
print(result)

print(
    '5. Дан список строк my_list. Создать новый список в который п оместитьэлементы из my_list у которых первый символ - буква "a".')

my_list = ["able", "bread", "about", "lesson", "hillel"]
list_a = []
my_list = " ".join(my_list)
for a in my_list.split():
    if a.startswith("a"):
        list_a.append(a)
print(list_a)

print(
    '6. Дан список строк my_list. Создать новый список в который поместитьэлементы из my_list в которых есть символ - буква "a" на любом месте.')

my_list = ["able", "bread", "about", "lesson", "hillel"]
list_a = []
my_list = " ".join(my_list)
for a in my_list.split():
    if "a" in a:
        list_a.append(a)
print(list_a)

print(
    '7. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).Например [1, 2, 3, "11", "22", 33]Создать новый список в который поместить только строки из my_list.')

my_list = [1, 2, 3, '11', '22']
new_list = []
for str_here in my_list:
    if type(str_here) == str:
        new_list.append(str_here)
print(new_list)

print(
    '8. Дана строка my_str. Создать список в который поместить те символы из my_str,которые встречаются в строке ТОЛЬКО ОДИН раз.')

my_str = "vkjs!fjn&jfnv????nfcj**"
result = []
for symbol in my_str:
    if my_str.count(symbol) == 1:
        result.append(symbol)
print(result)

print('9. Даны две строки. Создать список в который поместить те символы,которые есть в обеих строках хотя бы раз.')

str_1 = "vkjs!fjn&jfnv????nfcj**"
str_2 = "hbhebehv!dj**"
result = []
for symbol_1 in str_1:
    for symbol_2 in str_2:
        if symbol_1 == symbol_2:
            result.append(symbol_1)
print(result)

print(
    '10. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,но в каждой ТОЛЬКО ПО ОДНОМУ разу.Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s","d"], т.к. эти символы есть в каждой строке по одному разу')

str_1 = "aaaasdf1"
str_2 = "asdfff2"
result = []
for symbol_1 in str_1:
    for symbol_2 in str_2:
        if symbol_1 == symbol_2 and str_1.count(symbol_1) == 1 and str_2.count(symbol_2) == 1:
            result.append(symbol_1 and symbol_2)
print(result)

print(
    "11. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.Если строка содержит нечетное количество символов, пропущенный второй символ последней пары долженбыть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)")

my_str = "abcde"
result = []
if len(my_str) % 2:
    my_str = my_str + "_"
result = [my_str[i:i + 2] for i in range(0, len(my_str), 2)]
print(result)