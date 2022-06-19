s = input()
group0 = 0
group1 = 0

if s[0] == '0':
    group0 += 1
else:
    group1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i+1]:  # 이전 원소와 다르다면
        if s[i+1] == '1':  # 1로 바뀐다면
            group1 += 1
        else:  # 0으로 바뀐다면
            group0 += 1

print(min(group0, group1))
