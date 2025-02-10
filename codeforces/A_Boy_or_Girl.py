#https://codeforces.com/gym/586964/problem/A
def chat_or_not(strs):
    if len(set(strs)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    strs = input()
    chat_or_not(strs)
