


# def repeating(cipher, n):
#     s = ""
#     idx = 0
#     for i in range(1, n + 1):
#         s += cipher[idx]
#         idx += i
#         if idx >= n:
#             break
#     return s

# size = int(input())

# cipher = input()
# print(repeating(cipher,size))  








def repeat(cipher, l):
    s = ""
    idx = 0

    while idx <= l:
        for i in range(1, l+1):
            s += cipher[idx]
            idx += i
    return s
    # for i in range(1, l+1):
    #     s += cipher[idx]
    #     idx += i
    #     if idx >= l:
    #         break
    # return s


# if __name__ == "__main__":
l = int(input())
cipher = input()

print(repeat(cipher,l))