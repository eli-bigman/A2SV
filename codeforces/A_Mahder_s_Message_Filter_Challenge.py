def filter(n,s):
    s_rev = reversed(s)

    count = 0
    for ele in s_rev:
        if ele == ")":
            count+= 1
        else:
            break
    if count > (n - count):
        return "Yes"
    else:
        return "No"





if "__main__" == __name__:
    for _ in range(int(input())):
        n = int(input())
        s = input()
        print(filter(n,s))