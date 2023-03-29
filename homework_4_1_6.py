# В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.


if __name__ == '__main__':
    n=[int(i) for i in input('введите список чисел через пробел').split()]
    max=n.index(max(n))
    min=n.index(min(n))
    n[max],n[min] = n[min],n[max]
    print(' '.join(str(i) for i in n))
