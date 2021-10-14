import math
price = int(input())
pdiv3 = price
pdiv11 = price
div3 = math.floor(price/3)
div11 = math.floor(price/11)
pdiv3-=(3*div3)
pdiv11-=(11*div11)
print(pdiv3, pdiv11)