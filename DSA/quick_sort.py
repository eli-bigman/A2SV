def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
        


def  binary_search(arr, target):
    low , high = 0, (len(arr) -1)
    while low < high:
        mid = (low + high)//2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
            




if __name__ == "__main__":

    arr = [13,1,4,63,6,5,21,6]
    sorted_arr = quick_sort(arr)

    search = binary_search(sorted_arr, 21)

    print(sorted_arr, search)






# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Example
# print(quick_sort([64, 34, 25, 12, 22, 11, 90]))


# def  binary_search(arr, target):
#     len_arr = len(arr)
#     low, high = 0, len_arr - 1
#     mid = len_arr//2
#     while low <= high:
#         if target == mid:
#             return mid
#         elif target > mid:
#             low = mid + 1
#         else:
#             high = mid -1

        