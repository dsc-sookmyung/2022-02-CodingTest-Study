n = int(input())
data = list(map(int, input().split()))
data.sort()

if len(data) % 2 == 0:
    mid = len(data) // 2 - 1
else:
    mid = len(data) // 2

print(data[mid])
