'''
Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

'''
#!/bin/python3

import math
import os
import random
import re
import sys



def divisor(n):
    div = [i for i in range(1,n+1) if n%i==0]
    return max(div,key=lambda x: sum(int(i) for i in str(x)))

if __name__ == '__main__':
    n = int(input().strip())
    print(divisor(n))
