n = int(input())
num = []
bool = []

for i in range(n):
    x = int(input())
    num.append(x)

def prime(x):
    j = 0
    for i in range(1,x):
        if x%i == 0:
            j += 1
        elif x%i != 0:
            continue
    if j > 2:
        return 'F'
    elif j == 2:
        return  'T'

for j in num:
    if j != 2 and j%2 == 0:
        bool.append('F')
    elif j%2 != 0 or prime(j) == 'T' or j == 2:
        bool.append('T')

for k in bool:
    print(k)