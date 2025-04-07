
n, k, x = map(int, input().split())
work = list(map(int, input().split()))

normal_work_time = sum(work[:(n-k)])
total_work_time = normal_work_time + k * x

print(total_work_time)