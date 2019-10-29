from timeit import timeit

lst = [1, 2, 3, 1, 1, 1]

from random import randint
from collections import Counter
# print([x for x in lst if x != 1])

# print(list(filter(lambda x: x != 1, lst)))

# while 1 in lst:
#     lst.remove(1)
# print(lst)


res = [randint(1, 100) for x in range(10)]
Counter(res)


print(timeit('Counter([randint(1, 100) for x in range(10)])', setup='from random import randint\nfrom collections import Counter', number=1000))
