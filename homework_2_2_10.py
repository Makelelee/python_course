# Евгению предоставили строку, состоящую из русских букв разных регистров,
# и попросили очистить ее от заглавных литер. Как ему показалось,
# он написал верный код, но результат совсем не порадовал.
# Ниже представлен пример работы «чистильщика строк», которому срочно требуется ваша помощь.

if __name__ == '__main__':
    letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
    clean_string = ''
    for letter in letters:
        if not letter.isupper():
            clean_string += letter
    letters = clean_string
    print(letters)
