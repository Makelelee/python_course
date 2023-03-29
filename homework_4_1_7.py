# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.

import re
from collections import Counter
if __name__ == '__main__':
    t = '''\
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
'''
words = re.findall(r'\w+', t)
d = Counter(words)
ls = [k for k, v in d.most_common()]
print('\n'.join(ls))
