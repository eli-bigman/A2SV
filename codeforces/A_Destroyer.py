from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    def destroyer(arr,n):
        counter = dict(sorted(Counter(arr).items()))
        max_n = arr[-1]
        values = list(counter.values())

        if len(set(counter.keys())) != (max_n + 1):
            print("NO")
            return
        if not all(init >= prev for init,prev in zip(values, values[1:])):
            print("NO")
            return
        print("YES")

    destroyer(arr,n)



# clean version
# from collections import Counter

# def destroyer(arr):
#     counter = Counter(arr)  # Count occurrences
#     sorted_counts = sorted(counter.values())  # Get sorted values
    
#     # Check conditions
#     if len(counter.keys()) != max(counter.keys()) + 1 or any(sorted_counts[i] < sorted_counts[i - 1] for i in range(1, len(sorted_counts))):
#         return "NO"
#     return "YES"

# # Main loop
# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(destroyer(arr))



    
    



