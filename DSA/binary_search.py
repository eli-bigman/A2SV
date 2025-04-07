

def bianary_search(arr, target):
    arr = quicksort(arr)

    low , high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if target == arr[mid]:
           return mid
        elif target < arr[mid]:
           high= mid - 1
        else:
           low=mid +1
    return -1
           


def quicksort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    pivot = arr[len_arr//2]
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return quicksort(l)+m+quicksort(r)

    


if __name__ ==  "__main__":
    arr = [12,34,13,64,1,33,63,3]
    results = bianary_search(arr, 12)

    sorted_arr = quicksort(arr)

    print(results)
    print(sorted_arr)