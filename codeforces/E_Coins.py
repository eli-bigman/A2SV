for _ in range(int(input())):
    n,k = map(int,input().split())
    

    def cf_coins(n,k):
        if n % 2 == 0 or k % 2 != 0 :
            return "YES"
        return "NO"
    print(cf_coins(n,k))