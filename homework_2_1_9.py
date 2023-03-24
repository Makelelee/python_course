# Функция mul_to_int(a, b) может принимать целые или вещественные числа.
# Если результат умножения аргументов не имеет значимых чисел после запятой,
# то она возвращает его в виде целого числа.  В противном случае – в виде float.


def mul_to_int(a, b):
    result = a * b
    if float(result).is_integer():
        return int(result)
    return result


if __name__ == '__main__':
    print(mul_to_int(3, 8))
    print(mul_to_int(2.7, 14))
    print(type(mul_to_int(3, 8)))
    print(type(mul_to_int(2.7, 14)))

