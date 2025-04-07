
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
        for i in range(t):
            if arr[i] == 1:
                arr[i] += 1
        
            if arr[i + 1] % arr[i] == 0:
                arr[i + 1] += 1

        print(*arr)

# def lakshya():
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     for i in range(n):
#         if arr[i] == 1:
#             arr[i] += 1
    
#     for i in range(n - 1):
#         if arr[i + 1] % arr[i] == 0:
#             arr[i + 1] += 1
    
#     print(" ".join(map(str, arr)))

# def main():
#     import sys
#     input = sys.stdin.read
#     print(input)
#     data = input().split()
    
#     T = int(data[0])
#     index = 1
    
#     for _ in range(T):
#         n = int(data[index])
#         arr = list(map(int, data[index+1:index+1+n]))
#         index += n + 1
        
#         for i in range(n):
#             if arr[i] == 1:
#                 arr[i] += 1
        
#         for i in range(n - 1):
#             if arr[i + 1] % arr[i] == 0:
#                 arr[i + 1] += 1

        
#         print(" ".join(map(str, arr)))

# if __name__ == "__main__":
#     main()

        

