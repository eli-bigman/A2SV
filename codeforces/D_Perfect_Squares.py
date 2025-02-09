from math import sqrt

if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split()))  
    
    res = float("-inf")  
    
    for i in arr:
        if i < 0 or int(sqrt(i)) ** 2 != i:  
            res = max(res, i)  
    print(res)  