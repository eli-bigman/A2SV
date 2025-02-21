def triangle_stars(n):
    for i in range(1, n+1):
        print("*"*i)


if __name__ == '__main__':
    n = int(input())
    triangle_stars(n)