"""
Задание 1. Три списка
Даны три списка.
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
Нужно выполнить две задачи:
1. найти элементы, которые есть в каждом списке;
2. найти элементы из первого списка, которых нет во втором и третьем
списках.
Каждую задачу нужно выполнить двумя способами:
1. без использования множеств;
2. с использованием множеств.
"""

# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# for i in array_1 :
#     if i in array_2 and i in array_3 :
#         print("elements in every array", i)
        
# for i in array_1 :
#     if i in array_2 or i in array_3 :
#         continue    
#     else : print("elements in array_1 which are not in array_2 and array_3", i)

# array_1 = {1, 5, 10, 20, 40, 80, 100}
# array_2 = {6, 7, 20, 80, 100}
# array_3 = {3, 4, 15, 20, 30, 70, 80, 120}

# intersection_array = array_1 & array_2 & array_3

# print(list(intersection_array))

# difference_array = array_1 - array_2 -array_3

# print(list(difference_array))

"""
Задача 2. Палиндром
Пользователь вводит строку. Необходимо написать программу, которая
определяет, существует ли у этой строки перестановка, при которой она станет
палиндромом. Затем она должна выводить соответствующее сообщение.
"""

# print('enter a word or letters')
# str = input()
# def is_poly(string) :
#     unique = 0
#     for i in str :
#         if(str.count(i) % 2 != 0) :
#             unique += 1
#     if(unique <= 1) :
#         print("poly")
#     else :
#         print("not poly")
        
# is_poly(str)

"""
Задача 3. Словарь синонимов
Одна библиотека поручила вам написать программу для оцифровки словарей
синонимов. На вход в программу подаётся N пар слов. Каждое слово является
синонимом для своего парного слова.
Реализуйте код, который составляет словарь синонимов (все слова в словаре
различны), затем запрашивает у пользователя слово и выводит на экран его
синоним. Обеспечьте контроль ввода: если такого слова нет, выведите ошибку
и запросите слово ещё раз. При этом проверка не должна зависеть от регистра
символов.
"""

print('How many words in dictionary?')
dict_len = int(input())
def dict_maker (N) :
    dict = {}
    i = 0
    while i < N :
        i += 1
        print(f"enter {i} pair, example word1-word2 ")
        pair = input()
        dict_pair = pair.split("-")
        dict[dict_pair[0].lower()] = dict_pair[1].lower()
    return dict

dict = dict_maker(dict_len)

def find_key_in_dict (key, dict) :
    if key in dict:
        return dict[key]
    else:
        return "Key does not exist in the dictionary."
        
print("please enter word to search in dictionary")
word = input().lower()

print(find_key_in_dict(word,dict))
        
