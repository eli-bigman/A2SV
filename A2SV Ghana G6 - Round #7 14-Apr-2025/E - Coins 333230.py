# Problem: E - Coins - https://codeforces.com/gym/602997/problem/E

for _ in range(int(input())):
    n, k = map(int, input().split())
    
    if n % 2 == 0 or k % 2 != 0:  
        print("YES")
    else:
        print("NO")
