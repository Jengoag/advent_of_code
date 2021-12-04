f = open("day_01_data.txt", "r")

past = int(f.readline())
count = 0
for x in f:
    if int(x) > past:
        count = count + 1
    past = int(x)

print(count)