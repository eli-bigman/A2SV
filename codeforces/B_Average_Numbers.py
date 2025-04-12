n = int(input())
arr = list(map(int, input().split()))

def find_average(arr,n):
    average = sum(arr)/n
    if int(average) < average:
        print(0)
        return 
    else:
        average = int(average)

    count_avg = 0
    idx_avg = []

    for i in range(n):
        if arr[i] == average:
            count_avg += 1
            idx_avg.append(i+1)

    print(count_avg)
    print(*sorted(idx_avg))
    # return

find_average(arr,n)

