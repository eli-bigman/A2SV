

'''
Task
(space) delimiter and join using a — hyphen
You are given a string. Split the string on a
Function Description
Complete the split_and_join function in the editor below.
split_and_join has the following parameters:
• string line: a string Of space-separated words
Returns
• string: the resulting string
Input Format
The one line contains a String consisting Of space separated words.
Sample Input
this is a stri ng
Sample Output

'''
#----------------------------------------





def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
