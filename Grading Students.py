"""
Link problem --> https://www.hackerrank.com/challenges/grading/problem
"""

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    # Write your code here
    x = []
    for num in grades:

        if num % 5 == 0 and num >= 38:
            x.append(str(num))
        elif num % 5 == 3 and num >= 38:
            x.append(str(num + 2))
        elif num % 5 == 4 and num >= 38:
            x.append(str(num + 1))
        else:
            x.append(str(num))
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
