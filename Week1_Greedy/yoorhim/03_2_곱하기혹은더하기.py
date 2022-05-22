user = input()

result = int(user[0])

for i in range(1, len(user)):
    num = int(user[i])
    if num < 2 or result < 2:
        result += num
    else:
        result *= num

print(result)

