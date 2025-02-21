
def lucky_number(nums):
    seen = {}


    for i in range(nums[0], nums[1]):
        arr = sorted([int(k) for k in list(str(i))])
        lucky_num = arr[0] - arr[len(arr)]
        if lucky_num in seen:
            seen[lucky_num].append(i)
        else:
            seen[lucky_num] = [i]
    res = max(seen.keys)
    return 




if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        nums = list(map(int, input().split()))
        print(lucky_number(nums))