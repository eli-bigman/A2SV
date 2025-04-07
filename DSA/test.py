def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_sorted_arr(left, right)

def merge_sorted_arr(arr1,arr2):
    merged = []
    i=j=0
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] > arr2[j]:
            merged.append(arr2[j])
            j+=1
        else:
            merged.append(arr1[i])
            i+=1

    while i < len(arr1):
        merged.append(arr1[i])
        i+=1

    while j < len(arr2):
        merged.append(arr2[j])
        j+=1



    return merged





if __name__ == "__main__":

    import random
    random.seed("AC")
    arrays_list = [[random.randint(-10, 100) for _ in range(10)] for _ in range(3)]

    print(arrays_list)

    print("Sorted array -------------------------------------------")
    for array in arrays_list:
        print(merge_sort(array))
