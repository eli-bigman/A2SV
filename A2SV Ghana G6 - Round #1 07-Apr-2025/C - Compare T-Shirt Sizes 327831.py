# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585132/problem/C

def comp_size(a,b):
    weights = {"L":4,"M":3,"S":2, "X":1}
    def get_size(z):
        size = 0
        
        if z[-1] != "S":
            for i in z:
                size += weights[i]
            return size
        else:
            for i in z:
                size -= weights[i]
            return size
        
    
    if get_size(a) > get_size(b):
        return ">"
    elif get_size(a) < get_size(b):
        return "<"
    
    else:
        return "="
        
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a,b = map(str, input().split())
        print(comp_size(a,b))