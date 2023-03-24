# Напишите функцию pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел.


def pos_add(a, b):
    return abs(a + b)


if __name__ == '__main__':
    # a = 2
    # b = 5
    # print(a + b)
    # print(type(a + b))
    print(pos_add(2, 5))
    print(type(pos_add(2, 5)))
