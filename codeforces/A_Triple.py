
def triple(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
        if count[num] >= 3:
            return num
    return -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(triple(arr))