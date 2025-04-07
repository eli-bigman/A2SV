def one_and_two(arr,n):

    num_of_2 = arr.count(2)
    total = 0

    for i in range(n):
        if arr[i] == 2:
            total+=1
        if total == num_of_2 - total:
            return i + 1
    return -1
        
if "__main__" == __name__:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        
        print(one_and_two(arr,n))