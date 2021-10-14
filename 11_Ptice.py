a = ['A','B','C']
b = ['B','A','B','C']
g = ['C','C','A','A','B','B']
n = int(input())
anw = list(input())


for i in range(n):
    a.append(a[i])
    b.append(b[i])
    g.append(g[i])

def score(x):
    sc = 0
    for j in range(n):
        if x[j] == anw[j]:
            sc += 1
    return str(sc)

def search_sc(dict, lookup):
    for key, value in dict.items():
        for i in value:
            if lookup in i:
                return i

dict = {}
dict['Adrian'] = score(a)
dict['Bruno'] = score(b)
dict['Goran'] = score(g)

print(max(dict.values()))

seach_name = max(dict.values())
for name, sc in dict.items():
    if sc == seach_name:
        print(name)
