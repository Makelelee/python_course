# Напишите функцию superset(), которая принимает 2 множества.
# Результат работы функции: вывод в консоль одного из сообщений в зависимости от ситуации:
# 1 - «Супермножество не обнаружено»
# 2 – «Объект {X} является чистым супермножеством»
# 3 – «Множества равны»


def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 == set_2:
        print(f'Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print('Супермножество не обнаружено')


if __name__ == '__main__':
    set_1 = {1, 4, 3, 5}
    set_2 = {1, 4}
    set_3 = {1, 4, 3, 5}
    set_4 = {2, 15}
    superset(set_1, set_2)
    superset(set_1, set_3)
    superset(set_2, set_3)
    superset(set_4, set_2)
