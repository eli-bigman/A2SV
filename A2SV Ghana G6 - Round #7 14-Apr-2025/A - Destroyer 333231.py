# Problem: A - Destroyer - https://codeforces.com/gym/602997/problem/A

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    def destroyer(arr,n):
        counter = dict(sorted(Counter(arr).items()))
        keys = counter.keys()
        max_n = arr[-1]
        values = list(counter.values())

        if len(set(counter.keys())) != (max_n + 1):
            print("NO")
            return
        if not all(init >= prev for init,prev in zip(values, values[1:])):
            print("NO")
            return
        print("YES")
        
    destroyer(arr,n)


    
    



