def left_pyramid_stars(n):

    for i in range(1, n+1):
        if i % 2 == 1:
            rg = (n-i // 2)
            for i in range(rg):
                print(" ")
            print("*"*i)

            



if __name__ == '__main__':
    n = int(input())
    left_pyramid_stars(n)

