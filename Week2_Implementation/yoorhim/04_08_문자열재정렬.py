S = input()
arr_str = []
sum = 0

for i in range(len(S)):
    if S[i].isalpha():
        arr_str.append(S[i])
    else:
        sum += int(S[i])

arr_str.sort()
arr_str.append(str(sum))
result = ''.join(s for s in arr_str)
print(result)