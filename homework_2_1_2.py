# Обозначьте порядок вычисления выражения по операциям:
# 11 * 2 ** 2 – 13 / 4 + 7. Какое целое число получим в итоге?


def get_result_number(number):
    print(number)
    return number


if __name__ == '__main__':
    # a = 11 * 2 ** 2 - 13 / 4 + 7
    # print(a)
    # print(type(a))
    b = 2 ** 2
    c = 11 * b
    d = 13 / 4
    e = c - d
    g = e + 7
    print(g)
    print(type(g))

