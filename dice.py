import math
import random

def roll(sides):
    result = int(math.floor(random.random() * sides) +1)
    print result

