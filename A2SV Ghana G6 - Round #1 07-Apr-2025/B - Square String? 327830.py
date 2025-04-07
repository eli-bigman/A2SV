# Problem: B - Square String? - https://codeforces.com/gym/585132/problem/B

def square_s(s):
 
    if len(s) % 2 != 0:
        return "NO"
    
 
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