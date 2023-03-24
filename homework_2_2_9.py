# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.


def more_than_five(lst):
    new_lst = []
    for number in lst:
        if number > 5:
            new_lst.append(number)
    return new_lst


if __name__ == '__main__':
    print(more_than_five([10, 6, 41, 0]))
