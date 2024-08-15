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

print('enter a word or letters')
str = input()
def is_poly(string) :
    unique = 0
    for i in str :
        if(str.count(i) % 2 != 0) :
            unique += 1
    if(unique <= 1) :
        print("poly")
    else :
        print("not poly")
        
is_poly(str)