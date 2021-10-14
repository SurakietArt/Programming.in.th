n = int(input())
mook = []
clean_mook = []
for i in range(n):
    mook.append(input())
    mook.sort()

for j in mook:
    if j not in clean_mook:
        clean_mook.append(j)
    elif j in clean_mook:
        continue

for k in range(len(clean_mook)):
    print(clean_mook[k])


