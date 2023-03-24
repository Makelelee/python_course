# Напишите функцию to_float(num), которая преобразует любое число в число с плавающей точкой.
# Если в качестве аргумента передан другой тип данных, она возвращает «Невозможно преобразовать».


def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"


if __name__ == '__main__':
    print(to_float(10))
    print(to_float(7.749))
    print(to_float('еда'))
    print(type(to_float(12)))
    print(type(to_float(7.749)))
    print(type(to_float('еда')))
