for _ in range(int(input())):
    n = int(input())
    binary = list(input().split())
    
    
    if "101" in "".join([i for i in binary]):
        print("NO")
    else:
        print("YES")
    