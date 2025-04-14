# Problem: D - Cubes Sorting - https://codeforces.com/gym/602997/problem/D

def cube_sorting(arr,n):
    # max_sort = (n(n-1))/2 - 1

    if any(first <= second for first, second in zip(arr, arr[1:])):
        return "YES"
    return "NO"

#main loop
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(cube_sorting(arr,n))


