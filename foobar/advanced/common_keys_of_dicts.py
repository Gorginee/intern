import random
from functools import reduce

dict_a = {random.randint(1, 10): x for x in range(10)}
dict_b = {random.randint(1, 10): x for x in range(10)}
dict_c = {random.randint(1, 10): x for x in range(10)}
print(dict_a, dict_b, dict_c, sep='\n')

# solution one
set_a = set(dict_a)
set_b = set(dict_b)
set_c = set(dict_c)
print(set_a, set_b, set_c)
print(set.intersection(set_a, set_b, set_c))

# solution two
inter = []
for item in dict_a:
    if item in dict_b and item in dict_c:
        inter.append(item)
print(inter)

# solution three
print(reduce(lambda a, b: a & b, map(lambda d: d.keys(), [dict_a, dict_b, dict_c])))