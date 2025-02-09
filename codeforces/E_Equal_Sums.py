def sum_dict(arr):
    res = {}
    total = sum(arr)
    for idx,v in enumerate(arr):
        arr_sum = total - v
        res[idx] = arr_sum
    return res

def find_pairs(arrays):
    dict_list = []
    for arr in arrays:
        dict_list.append(sum_dict(arr))
    
    seen_values = {}
    res = []
    for i in range(len(dict_list)):
        for idx, s in dict_list[i].items():

            if s in seen_values:
                prev_seq, _ = seen_values[s]
                if prev_seq != i+1:
                    res.append((seen_values[s], (i+1, idx+1)))
                    return res
            seen_values[s] = (i+1, idx+1)
    return res

   







if __name__ == "__main__":
    n = int(input())
    arrays = []
    for _ in range(n):
        len_arr = int(input())
        arr = list(map(int, input().split()))
        arrays.append(arr)
        
    res = find_pairs(arrays)
    if res:
        print("YES")
        print(res[0][0][0], res[0][0][1])
        print(res[0][1][0], res[0][1][1])
    
    else:
        print("NO")




        

