# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.


def count_it(sequence):
    num_frequency = {int(item): sequence.count(item) for item in sequence}
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
    return dict(sorted_num_frequency[-3:])


if __name__ == '__main__':
    print(count_it('1111111111222'))
    print(count_it('123456789012133288776655353535353441111'))
    print(count_it('007767757744331166554444'))
