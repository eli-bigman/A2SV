"""
Given the participants' score sheet for University Sports Day, find the runner-up score.
Store the scores in a list and find the second highest score.

Input Format:
- First line: integer n, number of scores.
- Second line: array of n integers, scores separated by spaces.

Output Format:
- Print the runner-up score.

Sample Input:
5
2 3 6 6 5

Sample Output:
5

Explanation:
The list of scores is [2, 3, 6, 6, 5].
The highest score is 6, and the second highest is 5.
Hence, the runner-up score is 5.
"""


def runner_up(arr):
    array = [i for i in arr]
    first = max(array)
    arr_ = [i for i in array if i != first]
    return max(arr_)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # print(arr)
    print(runner_up(arr))
    
