'''
Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is
uncommon to use math.powO.
You are given three integers: a. b. and m. Print two lines.
On the first line. print the result of pow(a.b). On the second line. print the result of pow(a.b.m).
Input Format
The first line contains a. the second line contains b. and the third line contains m.
Constraints
1 S a S 10
10
2 < m < 1000
Sample Input
3
4
5
Sample Output
81
1

'''


#-----------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    
    print(pow(a,b))
    print(pow(a,b,m))


