import random as ran

ix = ran.randrange(1,101)
iy = ran.randrange(1,101)
print(ix)
print(iy)
loop = max(ix,iy)
gcd = []
for i in range(1, loop):
    if ix%i == 0 and iy%i == 0:
        gcd.append(i)
    elif ix%i != 0 and iy%i != 0:
        continue

print(max(gcd))