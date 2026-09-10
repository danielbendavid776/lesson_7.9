# use random -- seed
# 1
# try random seed between 1-42
#   random 10 int numbers between 1-100
#   check which seed gave the highest sum? print the seed and the sum
#  seed-1: [5, 7, 20, 90, ...] --> sum 217 ==> seed1: 217
#  seed-2: [4, 6, 53, 88, ...] --> sum 201 ==> seed2: 201
# 2
# make a function that gets a seed number, how many numbers to random, min_range, max_range --> returns sum
# write for loop that calls this function

import random

def sum_seed(seed):
    random.seed(seed)
    sum_10 = 0
    for i in range(1,11):
        random.randint(1, 100)
        sum_10 += random.randint(1, 100)
    return sum_10

max_sum = None
max_seed = None

for i in range(1,43):
    sum_fun = sum_seed(i)
    print(i, sum_fun)
    if max_sum is None or sum_fun > max_sum:
        max_sum = sum_fun
        max_seed = i
print()
print(max_seed , max_sum)

