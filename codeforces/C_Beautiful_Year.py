#https://codeforces.com/gym/586964/problem/C

if __name__ == "__main__":
    year = int(input())
    while True:
        year += 1
        if len(set(str(year))) == 4:
            print(year)
            break
        
    
             
