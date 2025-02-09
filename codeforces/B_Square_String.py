def square_s(s):
    # Check if the length is even
    if len(s) % 2 != 0:
        return "NO"
    
    # Compare the first and second halves
    mid = len(s) // 2
    if s[:mid] == s[mid:]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(square_s(s))
