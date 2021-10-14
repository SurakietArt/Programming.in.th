list = []
amount = int(input())

for i in range (1,amount+1):
    num = int(input())
    list.append(num)
print(min(list))
print(max(list))