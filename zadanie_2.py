# 1. Определите функцию get_list, которая принимает строку из целых чисел, разделенных пробелами, и возвращает список из этих чисел.
def get_list(string):
    return [int(x) for x in string.split()]

# 2. Создайте функцию sort_func, которая:
# a. Принимает функцию как аргумент
# b. Вызывает переданную функцию
# c. Сортирует результат работы функции по возрастанию
# d. Возвращает отсортированный результат
def sort_func(func):
    return sorted(func())

# 3. Используйте вызов функций get_list и sort_func, чтобы вывести результат на экран.
string = "3 1 4 1 5 9 2 6 5 3 5"
print(sort_func(get_list(string)))

