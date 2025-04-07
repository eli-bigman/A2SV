
def long_jumps(arr,n):
    # max_score = float('-inf')
    memo = [0] * n

    for i in range(n-1, -1,-1):
        if i + arr[i] < n:
            memo[i] = arr[i] + memo[i+ arr[i]]
        else:
            memo[i] = arr[i]
    return max(memo)




if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(long_jumps(arr, n))

