n = int(input())
list = list(input().split())
num = ''
j = 0


while min(list) == '0':
    list.pop(list.index(min(list)))
    j+=1

num += min(list)+('0'*j)
list.pop(list.index(min(list)))

while list != []:
    num += min(list)
    list.pop(list.index(min(list)))

print(num)