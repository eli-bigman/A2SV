
'''
Task
Given an integer. n. perform the following conditional actions:
• Ifn is Odd. print Wei rd
• If n is even and in the inclusive range of 2 to 5, print Not Wei rd
• If n is even and in the inclusive range Of 6 to 20, print Wei rd
• If n is even and greater than 20. print Not Wei rd
Input Format
A single line containing a positive integer, n.
Constraints
• 1 < n < 100
Output Format
Print Wei rd if the number is weird. Otherwise. print Not Wei rd.
Sample Input O
3
Sample Output O
Weird
Explanation O
n is odd and odd numbers are weird. so print Wei rd.

'''
#-------------------------------------------------------
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def weird_or_not(n):
    if n % 2 != 0:
        print("Weird")
        
    elif n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    weird_or_not(n)

