def pyramid_stars(n):

    for i in range(1, n+1):
        if i % 2 == 1:
            print(" "*(n-i // 2), "*"*i)
            

            



if __name__ == '__main__':
    n = int(input())
    pyramid_stars(n)
