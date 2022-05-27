n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1

for i in coin:
    if result < i:
        break
    result += i

print(result)