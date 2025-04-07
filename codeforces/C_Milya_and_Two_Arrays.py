for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = set()

    for a_val in a:
        for b_val in b:
            c.add(a_val + b_val)
    
    if len(c) >= 3:
        print("YES")
    else:
        print("NO")
