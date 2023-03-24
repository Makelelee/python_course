# Требуется определить индексы первого и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра:
# letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None),
# если же она есть, то кортеж будет состоять из первого и последнего индекса этого символа.


def first_last(letter, st):
    first_letter = st.find(letter)
    if first_letter < 0:
        return None, None
    last_letter = st.rfind(letter)
    return first_letter, last_letter


if __name__ == '__main__':
    print(first_last('q', 'wqertq'))
    print(first_last('x', 'xbvzxc'))
    print(first_last('f', 'gjdkso'))
