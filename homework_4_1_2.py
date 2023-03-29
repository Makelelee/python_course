# Напишите программу, которая будет запрашивать у пользователя целочисленные значения
# и сохранять их в виде списка. Индикатором окончания ввода значений должен служить ноль.
# Затем программа должна вывести на экран все введенные пользователем числа (кроме нуля) в порядке возрастания
# - по одному значению в строке. Используйте для сортировки либо метод sort, либо функцию sorted.


if __name__ == '__main__':
    data = []
    num = int(input("Введите целое число (0 для окончания ввода): "))
    while num != 0:
        data.append(num)
        num = int(input("Введите целое число (0 для окончания ввода): "))
    print(*sorted(data), sep='\r\n')
