'''

You are given a string and your task is to swap cases. In other words. convert all lowercase letters to
uppercase letters and vice versa.
For Example:
Www.HackerRank.com 
wh.hACKERrANK.COM
Pythonist 2
pYTHONIST 2
Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:
• string s: the string to modify
Retums
string: the modified string
Input Format
A single line containing a string s.
Constraints
O < ten(s) 1000


'''
#-----------------------------------------------------------------

def swap_case(s):
    res = []
    for i in s:
        if i.islower():
            i = i.upper()
            res.append(i)
        elif i.isupper:
            i = i.lower()
            res.append(i)
        else:
            res.append(i)
    return "".join(res)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
