#  Use random module to generate 5 random integers.

import random

random_numbers = []

for i in range(5):
    num = random.randint(1, 100)
    random_numbers.append(num)

print("Random integers:", random_numbers)
