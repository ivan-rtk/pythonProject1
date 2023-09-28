""" создайте вручную список с повторяюшимися элементами.
удалите из него все элементы, которые встречаются дважды"""

my_dict = {}
my_list = [1, 2, 1, 2, 5, 4, 7, 9, 4, 8]
new_list = []
for el in set(my_list):
    if my_list.count(el) == 1:
        new_list += [el]
my_list =new_list
print(my_list)