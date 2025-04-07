

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_array(left, right, arr)


def merge_two_sorted_array(arr1, arr2, final_arr):

    i = j= k = 0
    len_arr1 = len(arr1)
    len_arr2 =len(arr2)

    while i < len_arr1 and j < len_arr2:
        if arr1[i] <= arr2[j]:
            final_arr[k] = arr1[i]
            i+=1
        else:
            final_arr[k] = arr2[j]
            j+=1
        k+=1

    while i < len_arr1:
        final_arr[k] = arr1[i]
        i+=1
        k+=1
    while j < len_arr2:
        final_arr[k] = arr2[j]
        j+=1
        k+=1

    return final_arr




if __name__ == "__main__":

    import random
    random.seed("AC")
    arrays_list = [[random.randint(-10, 100) for _ in range(10)] for _ in range(3)]
    for array in arrays_list:
        print(merge_sort(array))



    # test_arr = [98, 59, 38, 8, 1, 18, 39, 4, 4, 51]
    # print(merge_sort(test_arr))