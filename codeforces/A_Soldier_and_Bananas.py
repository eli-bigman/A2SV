
def cost_of_bananas(w, k):
    sum_n = (w * (w+1))/2
    return int(sum_n) * k

if "__main__" == __name__:
    k,n,w = list(map(int, input().split()))

    cost = cost_of_bananas(w,k)
    if cost < n:
        print(0)
    else:
        print(cost - n)