num_list = []
modulo_list = []

for i in range(1,11):
    num = int(input())
    num_list.append(num)

for j in range(10):
    modulo = num_list[j] % 42
    modulo_list.append(modulo)

set_modulo_list = set(modulo_list)

print(len(set_modulo_list))