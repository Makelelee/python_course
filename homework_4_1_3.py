# Напишите программу, которая, как и в предыдущем случае, будет запрашивать у пользователя
# целые числа и сохранять их в виде списка. Индикатором окончания ввода значений также должен служить ноль.
# На этот раз необходимо вывести на экран введенные значения в порядке убывания.


if __name__ == '__main__':
    data = []
    num = int(input("Введите целое число (0 для окончания ввода): "))
    while num != 0:
        data.append(num)
        num = int(input("Введите целое число (0 для окончания ввода): "))
    print(*sorted(data, reverse=True), sep='\r\n')