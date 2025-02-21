
# def not_div(arr):
#     i = 0
#     j  = 1
#     n = len(arr)
#     count = 2 * n
#     op =0
    
#     while j < n:
#         if is_divisible() :
#             arr[i] += 1
#             arr[j]+= 1
#         i+=1
#         j+=1
#     return arr


# def is_divisible(n, k):
#     if n % k == 0:
#         return True
#     return False

#     # n = len(arr)

#     # for i in range(1, n):
#     #     while arr[i] % arr[i-1] == 0:
#     #         arr[i] += 1
    
#     # return arr



    

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        t = int(input())
        arr = list(map(int, input().split()))
        # res = not_div(arr)
        # ans = ""
        # print(*res)
        # # for i in res:
        # #     ans+= str(i)+ " "

        # # print(ans)
        op = 0
        i = 0
        
        while arr[i] % arr[i+1] == 0 and i < len(arr):
            arr[i]+= 1
            i+=1
            op+=1
        print(*arr)

        

