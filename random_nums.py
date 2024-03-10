import random
import math
#a program that randomly selects numbers in range from 1-9
list = []
for i in range(5):
    list.append(random.randrange(1,9))
for i in list:
    print(i)
    