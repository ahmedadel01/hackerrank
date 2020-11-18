import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    list_x = []
    list_loop = []
    if n == len(ar):
        for num in ar:
            if num not in  list_loop:
                list_loop.append(num)
                x = ar.count(num)
                if x >= 2:
                    y = x // 2
                    list_x.append(y)
    return sum(list_x)
  
                
            
if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    print(result)
