# Problem: E - From S To T - https://codeforces.com/gym/585132/problem/E

from collections import Counter

def can_transform(s, t, p):
    i, j = 0, 0  
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i != len(s):
        return False

    extra = Counter()
    i = 0  
    for char in t:
        if i < len(s) and char == s[i]:
            i += 1  
        else:
            extra[char] += 1

    available = Counter(p)
    for char, needed in extra.items():
        if available[char] < needed:
            return False

    return True

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        s = input().strip()
        t = input().strip()
        p = input().strip()
        print("YES" if can_transform(s, t, p) else "NO")
