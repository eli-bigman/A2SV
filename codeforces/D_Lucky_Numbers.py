
def lucky_number(nums):
    max_num = float('-inf')
    lucky = nums[0]

    for i in range(nums[0], nums[1]+1):

        elem = [int(s) for s in str(i)]

        if len(elem) > 1:
            lucky  = abs(elem[0] - elem[1])
        else:
            lucky  = abs(elem[0])

        
        max_num = max(max_num, i )

        if max_num == 9:
            break

    return lucky






    # for i in range(nums[0], nums[1]):
    #     arr = sorted([int(k) for k in list(str(i))])
    #     lucky_num = arr[0] - arr[len(arr)]
    #     if lucky_num in seen:
    #         seen[lucky_num].append(i)
    #     else:
    #         seen[lucky_num] = [i]
    # res = max(seen.keys)
    # return 




if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        nums = list(map(int, input().split()))
        print(lucky_number(nums))