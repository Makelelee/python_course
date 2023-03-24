from sys import getsizeof


# системы счисления (двоичная, 10, 16) - изучить основы!!!
# написать функцию, которая принимает число в 10 системе и новую систему 2 или 16, вывести результат и вернуть его.


def change_number_system(number, new_number_system):
    if new_number_system == 2:
        result = bin(number)
        # print(result)
        # return result
    elif new_number_system == 16:
        result = hex(number)
        # print(result)
        # return result
    else:
        result = "Wrong data"
        # print(result)
        # return result
    print(result)
    return result


# Сколько мегабайт памяти занимает число 3 ** 9090001?  Для решения воспользуйтесь функцией getsizeof() из модуля sys.


def get_amount_memory(number):
    result = getsizeof(number)
    result_mb = result / 1024 / 1024
    return result_mb


if __name__ == '__main__':
    # new_number_2 = change_number_system(5, 2)
    # print(new_number_2)
    # new_number_16 = change_number_system(20, 16)
    # print(new_number_16)
    # new_number_wrong = change_number_system(20, 8)
    # print(new_number_wrong)
    print(get_amount_memory(3**9090001))

