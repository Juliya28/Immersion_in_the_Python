# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18, 4, 6, 10]

my_list1 = []

for item in my_list:
    if my_list.count(item) > 1:
        if item not in my_list1:
            my_list1.append(item)
print(my_list1)