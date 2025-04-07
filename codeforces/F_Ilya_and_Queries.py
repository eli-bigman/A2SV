
def preprocessor(s: str) -> list[int]: 
    n = len(s)
    prefix = [0] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] + (1 if s[i] == s[i-1] else 0)
    return prefix

def solve(s: str, l: int, r: int ) -> int:
    prefix_sum = preprocessor(s)
    return prefix_sum[r-1]








s = input()
for _ in range(int(input())):
    l,r = map(int,input().split())
    # print(solve(s,l,r))
    print(preprocessor(s))