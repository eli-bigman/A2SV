n = int(input())
arr = list(map(int, input().split())) 
res = [0] * (n + 1)

for i in range(n):
    res[arr[i]] = i + 1

print(*res[1:])
    
