n,m,k = map(int, input().split())

def contest(n,m,k):
    return "Yes" if n <= m and n <= k else "No"

print(contest(n,m,k))

