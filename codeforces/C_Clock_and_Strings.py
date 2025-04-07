def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        if a > b:
            a, b = b, a
        u = a <= c <= b
        v = a <= d <= b
        print("YES" if u ^ v else "NO")

if __name__ == "__main__":
    main()