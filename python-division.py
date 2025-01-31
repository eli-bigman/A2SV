
'''
Task
The provided code stub reads two integers. a and b. from STDIN.
Add logic to print two lines. The first line should contain the result Of integer division. a // b. The second
line should contain the result of float division. a / b.
NO rounding or formatting is necessary.
Example
• The result Of the integer division 3/ = O.
• The result of the float division is 3/5 = 0.6.
Print:
0.6

'''

#-------------------------------------------------------------------------------------------------------------------


def divisor(a, b):
    
    print(a//b)
    print(a/b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    divisor(a, b)




