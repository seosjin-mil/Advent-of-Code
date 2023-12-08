ts = [52, 94, 75, 94]
ds = [426, 1373, 1279, 1216]
ans = []

for i in range(0, 4):
    count = 0
    for j in range(0, ts[i] + 1):
        if j * (ts[i] - j) > ds[i]:
            count = count + 1
    ans.append(count)

ret = 1
for i in ans:
    ret = ret * i

print(ret)
