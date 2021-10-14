#Input
x, y, z = input().split()
alp = input().upper()
#Convert to INT
ix = int(x)
iy = int(y)
iz = int(z)
#Convert to List
list_num = [ix,iy,iz]
list_alp = list(alp)
list_alp1 = list(alp) #For get Value from Dict
#List to Char
num3 = max(list_num)
list_num.remove(num3)
num1 = min(list_num)
list_num.remove(num1)
num2 = list_num[0]
C = max(list_alp)
list_alp.remove(C)
A = min(list_alp)
list_alp.remove(A)
B = list_alp[0]
#List to Dict
var = {A: num1, B: num2, C: num3}
print(var[list_alp1[0]],var[list_alp1[1]],var[list_alp1[2]])



