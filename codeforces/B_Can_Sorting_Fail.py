for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr == sorted(arr):
        print("NO")
    else:
        print("YES")