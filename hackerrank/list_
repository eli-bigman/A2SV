
"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of N followed by N lines of commands 
where each command will be of the types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

Example:
- append 1: Append 1 to the list, list = [1].
- append 3: Append 3 to the list, list = [1, 3].
- insert 2 2: Insert 2 at index 2, list = [1, 3, 2].
- print: Print the array, Output: [1, 3, 2].

Input Format:
The first line contains an integer, N, denoting the number of commands.
Each of the subsequent N lines contains one of the commands described above.

Constraints:
- The elements added to the list must be integers.

Output Format:
For each command of type print, print the list on a new line.

Sample Input 0:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""



def str_methods(x, lst):
    # lst = []
    action = list(x.split())
    
    if len(action) == 1 and action[0] != "print":
        method = action[0]
        exec(f'lst.{method}()')
        # print(lst)
    elif len(action) == 2:
        method = action[0]
        ele = int(action[1])
        exec(f'lst.{method}({ele})')
        # print(lst)
        
    elif len(action) == 3:
        method = action[0]
        idx = int(action[1])
        ele = int(action[2])
        exec(f'lst.{method}({idx},{ele})')
        # print(lst)
        
    elif len(action) == 1 and action[0] == "print":
        method = action[0]
        exec(f'{method}(lst)')
        
    return lst


if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        str_methods(input(), lst)
            
            
