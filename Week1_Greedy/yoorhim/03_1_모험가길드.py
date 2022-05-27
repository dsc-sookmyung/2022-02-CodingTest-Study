n = int(input())
guild = list(map(int, input().split()))
guild.sort()

result = 0
member = 0

for i in guild:
    member += 1
    if member >= i:
        result += 1
        count = 0

print(result)