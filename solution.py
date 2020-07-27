# Oh grasshopper, you're still a Googling programmer
#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce
from math import gcd

def lcm(x, y):
    return (x*y) // gcd(x,y)

def getTotalX(a, b):
    l = reduce(lcm, a, 1)
    g = reduce(gcd, b)
    temp = l
    count = 0

    while l <= g:
        if(g % l) == 0:
            count += 1
        l = l + temp

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
    fptr.close()
