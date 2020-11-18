"""
Given a time in 12 -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 

"""

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(S):
    # split input time
    h, m, s = map(int, S[:-2].split(':'))
    p = S[-2:]
    # convert time
    h = h % 12 + (p.upper() == 'PM') * 12
    
    return ('%02d:%02d:%02d') % (h, m, s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    result = timeConversion(S)

    f.write(result + '\n')

    f.close()
