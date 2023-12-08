t = 52947594
d = 426137412791216
count = 0

for i in range(0, t + 1):
    if i * (t - i) > d:
        count = count + 1

print(count)
