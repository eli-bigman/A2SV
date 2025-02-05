"""
Given three integers x, y, z representing the dimensions of a cuboid, 
and an integer n, print a list of all possible coordinates (i, j, k) on a 3D grid 
where the sum of i + j + k is not equal to n. Use list comprehensions.

Input Format:
- Four integers: x, y, z, n, each on a separate line.

Output Format:
- Print the list of coordinates in lexicographic increasing order.

Sample Input 0:
1
1
1
2

Sample Output 0:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation:
Each variable x, y, z will have values of 0 or 1.
All permutations of lists are generated. Remove arrays that sum to 2.

Sample Input 1:
2
2
2
2

Sample Output 1:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], 
 [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], 
 [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], 
 [2, 2, 1], [2, 2, 2]]
"""



def get_pem(x,y,z,n):
    arr = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
    res = [i for i in arr if sum(i) != n]
    return res

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print(get_pem(x,y,z,n))
