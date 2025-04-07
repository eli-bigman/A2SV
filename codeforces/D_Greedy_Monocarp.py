for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    s = 0
    for i in arr:
        s += i
        if s > k:
            s -= i
            break
    print(k - s)
        
