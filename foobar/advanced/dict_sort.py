import random


stores = {x: random.randint(60, 100) for x in range(1, 43)}


print(sorted(stores.items(), key=lambda x: x[1]))

print(sorted(zip(stores.values(), stores.keys())))