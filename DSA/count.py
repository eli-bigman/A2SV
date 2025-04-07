Input = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 7, 7, 8, 8, 10]
def count_k_logn(arr):
    curr_idx = 0
    cnts = 0
    
    while curr_idx < len(arr):
        cnts += 1
        
        h = arr[curr_idx]
        
        left, right = curr_idx, len(arr)-1
        last_true = -1
        
        while left <= right:
            mid = int((left + right)/2)
            
            if arr[mid] <= h:
                last_true = mid
                left = mid + 1
            else:
                right = mid-1
                
        curr_idx = last_true + 1
        
    return cnts


results = count_k_logn(input)
print(results)
