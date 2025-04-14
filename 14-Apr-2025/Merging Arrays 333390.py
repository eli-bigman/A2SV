# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

def mergeSort(arr1, arr2):
    merge = []
    i = 0
    j = 0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i+=1

        else:
            merge.append(arr2[j])
            j+=1

    merge.extend(arr1[i:])
    merge.extend(arr2[j:])


    return merge

print(*mergeSort(arr1,arr2))
