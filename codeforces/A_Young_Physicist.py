# for _ in range(int(input())):

n = int(input())
cord = [list(map(int, input().split())) for _  in range(n)]



def sum_forces(matrix):
    x_sum, y_sum, z_sum = map(sum, zip(*matrix))
    
    if x_sum == 0 and y_sum == 0 and z_sum == 0:
        return "YES"
    return "NO"


print(sum_forces(cord))


    
        