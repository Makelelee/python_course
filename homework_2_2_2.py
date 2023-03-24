# Имеется список с произвольными данными. Поставлена задача преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Функция list_to_set() выводит на печать получившееся множество.


from collections.abc import Hashable


def list_to_set(note):
    st = {item for item in note if isinstance(item, Hashable)}
    print(st)


if __name__ == '__main__':
    list_to_set([1, [2], 3, 22, 9, (3, 5)])
