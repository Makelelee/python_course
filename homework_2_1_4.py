# Используя стандартные арифметические операции представьте самое большое целое
# число из цифр 4, 4, 4 и приведите его значение.


def get_largest_number(number):
    print(number)
    return number


if __name__ == '__main__':
    a = 4 + 4 + 4
    b = 4 * 4 * 4
    c = 4 ** 4 ** 4
    d = 4 - 4 - 4
    e = 4 / 4 / 4
    number_list = [a, b, c, d, e]
    max_number = max(number_list)
    print("Наибольшее число:", max_number)

