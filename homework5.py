immutable_var = ([5, 6, 15], "potato", 3.9)
print(immutable_var, "- весь кортеж")
print(immutable_var[0][2], "- третья часть первого элемента кортежа")
print(immutable_var[-1], "- последний элемент кортежа")

# immutable_var[1] = 76 - изменить значение 6 внутри кортежа на значение 76 не получится. В данном примере в кортеже
# находятся элементы типов: list, string, float и изменить мы сможем только переменные значения внутри списка(первый
# элемент), все остальные значения изменить нельзя, они будут постоянными на протяжении всего кода.

mutable_list = [14, 13.5, False, "Meteor"]
print(mutable_list, "- изначальный список")
mutable_list[0] = "Hello"
mutable_list[1] = 1000
mutable_list.remove(False)
mutable_list = mutable_list[::-1]
print(mutable_list, "- измененный список")
