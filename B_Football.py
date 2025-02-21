def football(n):
    # stack = []
    
 
    if "1111111" in n or "0000000" in n:
        
        return "YES"
    else:
        
        return "NO"
        
    # print("NO")

if __name__ == "__main__":
    n = input()
    print(football(n))


    # print("".join(stack[:7])